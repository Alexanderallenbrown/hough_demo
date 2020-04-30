import cv2
import numpy as np
## Read image as gray-scale
img = cv2.imread('buttons.jpg', cv2.IMREAD_COLOR)
print img.shape

gimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gimg = cv2.medianBlur(img,5)
#edge filter to get a black and white image
canny = cv2.Canny(gimg, 200, 200)
#detector must work only on canny (edge) image.
circles = cv2.HoughCircles(canny,cv2.cv.CV_HOUGH_GRADIENT,1,20,
                            param1=120,param2=80,minRadius=5,maxRadius=200)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

#this shows an image, but doesn't work on rosDS
# cv2.imshow('detected circles',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#save output image
cv2.imwrite("output.jpg",img)
cv2.imwrite("canny.jpg",canny)