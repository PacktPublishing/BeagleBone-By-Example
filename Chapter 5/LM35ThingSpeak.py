import Adafruit_BBIO.ADC as ADC
import time
import requests
ADC.setup()
 
while True:
    reading = ADC.read('P9_40')
    millivolts = reading * 1800  
    temp_c = millivolts / 10
    print temp_c
    r = requests.post('https://api.thingspeak.com/update.json', data = {'api_key':'2V62DORS5O40Q1TL','field1':temp_c})
    if str(r) == "<Response [200]>":
	print "Data Updated to Cloud"
    else:
	print "Error"
	print "r = ", r
    time.sleep(61)
