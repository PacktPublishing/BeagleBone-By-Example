import time                                                                     
from itertools import cycle                                                     
from flask import Flask, render_template                                        

import Adafruit_BBIO.GPIO as GPIO
GPIO.setup("P8_18", GPIO.OUT)
GPIO.setup("P8_16", GPIO.OUT)
GPIO.setup("P8_14", GPIO.OUT)
GPIO.setup("P8_12", GPIO.OUT)

app = Flask(__name__)                                            

@app.route("/")                                                                 
@app.route("/<state>")                                                          
def update_lamp(state=None):                                                    
    if state == 'F':                                                           
        print "Robot Moving Forward"
	GPIO.output("P8_18", GPIO.HIGH)
        GPIO.output("P8_16", GPIO.LOW)
        GPIO.output("P8_14", GPIO.HIGH)
        GPIO.output("P8_12", GPIO.LOW)
        time.sleep(.2)                                                          
    if state == 'R':                                                          
        print "Robot Turning Right"
	GPIO.output("P8_18", GPIO.HIGH)
        GPIO.output("P8_16", GPIO.LOW)
        GPIO.output("P8_14", GPIO.LOW)
        GPIO.output("P8_12", GPIO.LOW)                                                          
        time.sleep(.2)
    if state == 'L':
        print "Robot Turning Left"
        GPIO.output("P8_18", GPIO.LOW)
        GPIO.output("P8_16", GPIO.LOW)
        GPIO.output("P8_14", GPIO.HIGH)
        GPIO.output("P8_12", GPIO.LOW)
        time.sleep(.2)
    if state == 'S':
        print "Robot Stopped"
        GPIO.output("P8_18", GPIO.LOW)
        GPIO.output("P8_16", GPIO.LOW)
        GPIO.output("P8_14", GPIO.LOW)
        GPIO.output("P8_12", GPIO.LOW)
        time.sleep(.2)                 
    template_data = {                                                           
        'title' : state,                                                        
    }                                                                           
    return render_template('Robot.html', **template_data)

if __name__ == "__main__":                                                      
    app.run(debug=True, host='0.0.0.0')
