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
laststate = "Temperature High" 

import smtplib
to = 'letsplaywitharduino@gmail.com'
gmail_user = 'jayakarthigeyan@gmail.com'
gmail_pwd = '##!$@%8'
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)
try:	
	while True:
		reading = ADC.read('P9_40')
		millivolts = reading * 1800  
		temp_c = millivolts / 10
		if (temp_c > 50) and laststate == "Temperature Low":
			print "Temperature is high"
			GPIO.output(RedLED, GPIO.HIGH)
			GPIO.output(GreenLED, GPIO.LOW)
			header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:Temperature Alert from BeagleBone\n'
			msg = header + '\n BeagleBone sensed that the temperature is high\n\n'
			smtpserver.sendmail(gmail_user, to, msg)
			laststate = "Temperature High"
		if (temp_c < 50) and laststate == "Temperature High":
			print "Temperature is normal"
			GPIO.output(RedLED, GPIO.LOW)
                        GPIO.output(GreenLED, GPIO.HIGH)
			header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:Temperature Alert from BeagleBone\n'
                        msg = header + '\n BeagleBone sensed that the temperature is low\n\n'
			smtpserver.sendmail(gmail_user, to, msg)
			laststate = "Temperature Low"
		time.sleep(1)

except KeyboardInterrupt:
    print "Keyboard Interrupt"
    GPIO.cleanup()
    print "GPIO Cleaned"
    smtpserver.close()
    print "Email logged out"
