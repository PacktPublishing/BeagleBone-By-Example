import time
import Adafruit_BBIO.GPIO as GPIO
GPIO.setup("P9_12", GPIO.OUT)
try:
    while True:
        print "Blinking"
	GPIO.output("P9_12", GPIO.HIGH)
        time.sleep(5)
        GPIO.output("P9_12", GPIO.LOW)
        time.sleep(5)

except KeyboardInterrupt:
    print "Keyboard Interrupt"
    GPIO.cleanup()
    print "GPIO Cleaned"
