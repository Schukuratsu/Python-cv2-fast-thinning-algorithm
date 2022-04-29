  # Importing the required modules. 
import numpy as np
import cv2
import ftlib as ft

  # Reading the image as binary format and storing it in a variable. 
img = cv2.imread('test_image.tif',0) #binary image
  # Storing the thinned image in a variable.
thinned_image = ft.fastThin(img)
  # Displaying the original image.
cv2.imshow('original image',img)
  # Displaying the thinned image. 
cv2.imshow('thinned image',thinned_image) 
cv2.waitKey(0) # press any key to close
  # Destroys all the windows formed for displaying the images.
cv2.destroyAllWindows()
