import Adafruit_BBIO.GPIO as GPIO
import time
GPIO.setup("P9_27", GPIO.IN)
while True:
	print GPIO.input("P9_27")
	time.sleep(0.5)
