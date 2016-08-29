import cv2 # Importing OpenCV python Library
import time #Import Time Library
import os #Import OS Library
import smtplib #Import SMTP Library
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
gmail_user = "jayakarthigeyan@gmail.com" #Sender email address
gmail_pwd = "!@#$%^&*()" #Sender email password
to = "jayakarthigeyan@gmail.com" #Receiver email address
subject = "Security Breach" #Subject of Email
text = "There is some activity in your home. See the attached picture." #Text Content of Email
import Adafruit_BBIO.GPIO as GPIO # Import Adafruit GPIO Library
GPIO.setup("P9_12", GPIO.IN) # Setup GPIO60 / P9_12 as Input Pin
GPIO.add_event_detect("P9_12", GPIO.RISING) # Create a event to detect Rising pulse on GPIO60
try:
    while True:
        if GPIO.event_detected("P9_12"): #If RISING event detected
            print "Movement Detected"  #prints out text saying Movement Detected
            cap = cv2.VideoCapture(0) #initialize the camera capture object with the cv2.VideoCapture class with index of camera 0 i.e. video0
            cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 352) #set property for camera, frame width
            cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 288) #set property for camera, frame height
            print "Capturing Image"
            ret, frame = cap.read() #read and capture the frame
            print "Saving Image"
            cv2.imwrite('Photo.jpg', frame) #save the captured image
            del(cap) #delete the camera object that was created before exiting program
            print "Sending email"
            picname = 'Photo.jpg'
            attach = picname # Attach the Saved Photo.jpg
            msg = MIMEMultipart()
            msg['From'] = gmail_user
            msg['To'] = to
            msg['Subject'] = subject
            msg.attach(MIMEText(text))
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(open(attach, 'rb').read())
            Encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' %os.path.basename(attach))
            msg.attach(part)
            mailServer = smtplib.SMTP("smtp.gmail.com", 587)
            mailServer.ehlo()
            mailServer.starttls()
            mailServer.ehlo()
            mailServer.login(gmail_user, gmail_pwd)
            mailServer.sendmail(gmail_user, to, msg.as_string())
            mailServer.close()
            print "Email Sent"
            os.remove(picname)
        time.sleep(0.05) #loop every 50 miliseconds to not overburden the CPU
except KeyboardInterrupt:
    print "Keyboard Interrupt"
    GPIO.cleanup()
    print "GPIO Cleaned"

