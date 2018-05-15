import numpy as np
import cv2
import ftlib as ft

img = cv2.imread('example.tif',0) #binary image
thinned_image = ft.fastThin(img)
cv2.imshow('original image',img)
cv2.imshow('thinned image',thinned_image)
cv2.waitKey(0) # press any key to close
cv2.destroyAllWindows()
