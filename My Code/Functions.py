import cv2 as cv

### Original
img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow("Cat",img)

#Grayscale
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",grey)

#Blur
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)

#Edge
canny = cv.Canny(img,125,175)
cv.imshow("Canny Edge",canny)

#Edge Cascade Blur
canny = cv.Canny(blur,125,175)
cv.imshow("Canny Edge Blur",canny)

## Dilating the image
dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow("Dilated",dilated)

##Eroded
eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow("Eroded",eroded)

#Resize
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("Resize",resized)

#Cropping
cropped = img[50:200,200:400]
cv.imshow("Crop",cropped)

cv.waitKey(0)