import cv2
import numpy as np
from time import sleep
import glob

files = glob.glob('./input/*')
print(files)
count = 0
for fname in files:
    
    img = cv2.imread(fname)
    fx = 0.4
    fy = 0.4
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,np.array([80,30,0]),np.array([160,255,255]))
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    output = cv2.drawContours(img,contours,-1,(255,255,255),-1)
    cv2.imwrite('output/'+str(count)+".png",output)
    cv2.imshow("test",cv2.resize(mask,fx=fx,fy=fy,dsize=None))
    count = count+1
    cv2.waitKey(0)