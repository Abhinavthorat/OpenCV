import cv2 as cv
import numpy as np


blank = np.zeros((500,500,3),dtype='uint8')


cv.imshow('Blank',blank)

img = cv.imread('../Resources/Photos/cat.jpg')
cv.imshow('Cat',img)


blank[200:300,300:400] = 0,255,0
cv.imshow('Green',blank)

cv.rectangle(blank,(0,0),(blank.shape[0]//2,blank.shape[0]//2),(255,0,0),thickness=cv.FILLED)

cv.imshow('Rectangle',blank)

cv.circle(blank,(250,250),40,(0,0,255),-1)

cv.imshow('Circle',blank)

cv.line(blank,(0,0),(250,250),(255,255,255),10)
cv.imshow("Line",blank)




cv.putText(blank,"Hello",(25,250),cv.FONT_HERSHEY_TRIPLEX,2,(0,0,255))
cv.imshow("Text",blank)
cv.waitKey(0)