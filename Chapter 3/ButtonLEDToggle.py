import Adafruit_BBIO.GPIO as GPIO
import time
 
GPIO.setup("P9_27", GPIO.IN)
GPIO.setup("P9_30", GPIO.OUT)
GPIO.output("P9_30", GPIO.LOW)
 
old_switch_state = 0
ledstate = 0
 
while True:
    new_switch_state = GPIO.input("P9_27")
    if new_switch_state == 1 and old_switch_state == 0 :
	if ledstate == 0:
		GPIO.output("P9_30", GPIO.HIGH)
		print "Led On"
		ledstate = 1
	else:
		GPIO.output("P9_30", GPIO.LOW)
		print "Led Off"
		ledstate = 0
        time.sleep(0.1)
    old_switch_state = new_switch_state
