import time                                                                     
from itertools import cycle                                                     
from flask import Flask, render_template                                        

app = Flask(__name__)                                            

@app.route("/")                                                                 
@app.route("/<state>")                                                          
def update_lamp(state=None):                                                    
    if state == 'on':                                                           
        print "Button 'On' was clicked"
        time.sleep(.2)                                                          
    if state == 'off':                                                          
        print "Button 'Off' was clicked"                                                          
        time.sleep(.2)                 
    template_data = {                                                           
        'title' : state,                                                        
    }                                                                           
    return render_template('main.html', **template_data)

if __name__ == "__main__":                                                      
    app.run(debug=True, host='0.0.0.0')
