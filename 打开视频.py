# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 14:01:34 2018

@author: king
"""



import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while(1):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()