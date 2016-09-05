import numpy as np 
import cv2
from matplotlib import pyplot as plt 
img =cv2.imread('messi.jpg',0)
edges=cv2.Canny(img,100,200)
cv2.imshow('image',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
#plt.subplot(121),plt.imshow(img,cmap = 'gray')
#plt.title('Orginal'),plt.xticks([]),plt.yticks([])
#plt.subplot(122),plt.imshow(edges,cmap = 'gray')
#plt.title('Edge'),plt.xticks([]),plt.yticks([])