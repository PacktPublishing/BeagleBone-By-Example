import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
import time

RedLED = "P9_27"
GreenLED = "P9_30"
GPIO.setup(RedLED, GPIO.OUT)
GPIO.setup(GreenLED, GPIO.OUT)
GPIO.output(RedLED, GPIO.LOW)
GPIO.output(GreenLED, GPIO.LOW)

ADC.setup()

try:	
	while True:
		reading = ADC.read('P9_40')
		millivolts = reading * 1800  
		temp_c = millivolts / 10
		if (temp_c > 50):
			print "Temperature is high"
			GPIO.output(RedLED, GPIO.HIGH)
			GPIO.output(GreenLED, GPIO.LOW)
		if (temp_c < 50):
			print "Temperature is normal"
			GPIO.output(RedLED, GPIO.LOW)
                        GPIO.output(GreenLED, GPIO.HIGH)
		time.sleep(1)

except KeyboardInterrupt:
    print "Keyboard Interrupt"
    GPIO.cleanup()
    print "GPIO Cleaned"
