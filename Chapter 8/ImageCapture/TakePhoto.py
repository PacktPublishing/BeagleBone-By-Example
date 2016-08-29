import cv2 # Importing OpenCV python library
cap = cv2.VideoCapture(0) #initialize the camera capture object with the cv2.VideoCapture class with index of camera 0 i.e. video0
cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 352) #set property for camera, frame width
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 288) #set property for camera, frame height
print "Capturing Image"
ret, frame = cap.read() #read and capture the frame
print "Saving Image"
cv2.imwrite('Photo.jpg', frame) #save the captured image 
del(cap) #delete the camera object that was created before exiting program
