import time                                                                     
from itertools import cycle                                                     
from flask import Flask, render_template                                        

import Adafruit_BBIO.GPIO as GPIO
GPIO.setup("P9_12", GPIO.OUT)

app = Flask(__name__)                                            

@app.route("/")                                                                 
@app.route("/<state>")                                                          
def update_lamp(state=None):                                                    
    if state == 'on':                                                           
        print "Bulb was turned on"
        GPIO.output("P9_12", GPIO.HIGH)
        time.sleep(.2)                                                          
    if state == 'off':                                                          
        print "Bulb was turned off"
        GPIO.output("P9_12", GPIO.LOW)                                                          
        time.sleep(.2)
    template_data = {                                                           
        'title' : state,                                                        
    }                                                                           
    return render_template('main.html', **template_data)

if __name__ == "__main__":                                                      
    app.run(debug=True, host='0.0.0.0')
