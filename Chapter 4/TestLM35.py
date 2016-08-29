import Adafruit_BBIO.ADC as ADC
import time

ADC.setup()
 
while True:
    reading = ADC.read('P9_40')
    millivolts = reading * 1800  
    temp_c = millivolts / 10
    print temp_c
    time.sleep(1)
