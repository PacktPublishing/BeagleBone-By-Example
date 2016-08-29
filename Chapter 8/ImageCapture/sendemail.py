import os #imports os module which is helpful for working with files and directories
import smtplib # Import smtplib module defines an SMTP client session object 
               # that can be used to send mail to any Internet machine using SMTP
from email.MIMEMultipart import MIMEMultipart # MIME Modules are used for 
from email.MIMEBase import MIMEBase           # message structuring and encryption
from email.MIMEText import MIMEText           # of email content
from email import Encoders # Helps in Encoding the message payload
gmail_user = "jayakarthigeyan@gmail.com" #Sender email address
gmail_pwd = "@#!$%^&*()" #Sender email password
to = "jayakarthigeyan@gmail.com" #Receiver email address
subject = "Test Email with Attachment" #Subject of the email we are going to send
text = "Hi, this is the content of the email" #This is the content text of the email
attach = 'Photo.jpg' #Attachment we are going to attach to the email
msg = MIMEMultipart() # Creates message structure
msg['From'] = gmail_user # In the message structure sets the gmail sender email address 
msg['To'] = to # In the message structure sets the gmail receiver email address
msg['Subject'] = subject # In the message structure sets the subject field
msg.attach(MIMEText(text)) # Your message as text format
part = MIMEBase('application', 'octet-stream') # Creates the message into a binary file
part.set_payload(open(attach, 'rb').read()) # Sets the entire message object's payload
Encoders.encode_base64(part) # Encodes the message
part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(attach))
msg.attach(part) # Attaches the message payload to email message
mailServer = smtplib.SMTP("smtp.gmail.com", 587) # Connect to email server
mailServer.ehlo() # Send first request to server 
mailServer.starttls() # Test SMTP configuration 
mailServer.ehlo() 
mailServer.login(gmail_user, gmail_pwd) # Login into server with sender email and password
mailServer.sendmail(gmail_user, to, msg.as_string()) # Send email message
mailServer.close() # Close server connection
print "Email Sent" # Print text "Email Sent" on console
