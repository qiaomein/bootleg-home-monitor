
# import the opencv library
import cv2
import numpy as np
import time
from sms import send_sms


  
# define a video capture object
vid = cv2.VideoCapture(0)

threshold = 10
t0 = time.time()
g0 = None
buffer = []

while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    g = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elapsed = time.time() - t0

    cost = g - g0



    # Display the resulting frame
    cv2.imshow('frame', gray)
    
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()