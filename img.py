
import cv2
from PIL import Image
from this import get_range

orange=[0,165,255]
c=cv2.VideoCapture(0)

while True:
    ret,frame=c.read()
    diff_img=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lowerlimit,upperlimit=get_range(color=orange)
    
    
    mask=cv2.inRange(diff_img,lowerlimit,upperlimit)
    
    mask_=Image.fromarray(mask)  #converting to pillow from np array so that it gets easier to get bounding box.
    
    boundingbox=mask_.getbbox()
    #print(boundingbox)
    if boundingbox is not None:
        x1,y1,x2,y2=boundingbox
        
        frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)
        
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1)& 0xFF==ord('q'):
        break
    
c.release()

cv2.destroyAllWindows()