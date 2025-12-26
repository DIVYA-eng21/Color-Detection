import numpy as np
import cv2

def get_range(color):
    cc=np.uint8([[color]])
    hsv=cv2.cvtColor(cc,cv2.COLOR_BGR2HSV)
    
    lowerlimit=hsv[0][0][0]-10,100,100
    upperlimit=hsv[0][0][0]+10,255,255
    
    lowerlimit=np.array(lowerlimit,dtype=np.uint8)
    upperlimit=np.array(upperlimit,dtype=np.uint8)
    
    return lowerlimit,upperlimit
