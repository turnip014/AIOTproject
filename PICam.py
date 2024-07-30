## REQUIREM ##
#pip install pyzbar -> Could be diff for Linux pls adv
#pip install numpy
#pip install opencv-python
#Trust Author

import cv2
import numpy as np
from pyzbar.pyzbar import decode

scan = cv2.VideoCapture(2) #Find ID of camera

while True:
    success , img = scan.read() #Define success criterion
    if not success:
        break
        
    for code in decode(img):  
        print(code.data.decode("utf-8"))

    cv2.imshow("image", img)
    cv2.waitKey(10) #Milleseconds per scan

