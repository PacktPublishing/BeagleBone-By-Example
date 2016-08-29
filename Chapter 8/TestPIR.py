import time #Import Time Module
import Adafruit_BBIO.GPIO as GPIO # Import Adafruit GPIO Library
GPIO.setup("P9_12", GPIO.IN) # Setup GPIO60 / P9_12 as Input Pin
GPIO.add_event_detect("P9_12", GPIO.RISING) # Create a event to detect Rising pulse on GPIO60

try:
    while True:
        if GPIO.event_detected("P9_12"): #If RISING event detected
            print "Movement Detected"  #prints out text saying Movement Detected
        time.sleep(0.05) #loop every 50 miliseconds to not overburden the CPU

except KeyboardInterrupt:
    print "Keyboard Interrupt"
    GPIO.cleanup()
    print "GPIO Cleaned"
