import Adafruit_BBIO.GPIO as GPIO
import time
 
GPIO.setup("P9_27", GPIO.IN)
 
old_switch_state = 0
 
while True:
    new_switch_state = GPIO.input("P9_27")
    if new_switch_state == 1 and old_switch_state == 0 :
        print('Button pressed!')
        time.sleep(0.1)
    old_switch_state = new_switch_state
