import cv2
import numpy as np 
print ('Hello')
img = cv2.imread('messi.jpg',0)
cv2.imshow('image',img)
cv2.imwrite('messigray.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()