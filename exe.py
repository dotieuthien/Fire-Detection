"""
Author: Do Tieu Thien
Date: 06/11/1017
"""
"""Import"""
import cv2
import numpy as np
from fnc.HSI import HSI
from fnc.RGB_model import RGB_model

"""Init"""
image= cv2.imread('Image/2.jpg')
image = np.double(image) # Double typr for Calculation
size = np.shape(image)
Thres_R = 140# Threshold of Red

""" Condition 1: Colour model of flames """
# Apply RGB colour model
im = RGB_model(image,Thres_R)
# Convert image into HSI colour space
im_HSI = HSI(im)
H = im_HSI[:,:,0]
S = im_HSI[:,:,1]
I = im_HSI[:,:,2]
# Condition of flames pixel:
im_HSI_temp = np.zeros([size[0],size[1]])
im_HSI_temp[:,:] = ((H[:,:] >= 0) & (H[:,:] <= 60)) & ((S[:,:] >= 0.4) & (S[:,:] <= 1)) & ((I[:,:] >= 127) & (I[:,:] <= 255))
im_HSI[:,:,0] = im_HSI_temp[:,:]
im_HSI[:,:,1] = im_HSI_temp[:,:]
im_HSI[:,:,2] = im_HSI_temp[:,:]
image_1 = np.uint8(im_HSI*image)
# Display image
cv2.imshow('image',image_1)
cv2.waitKey(0)
cv2.destroyAllWindows()

""" Condition 2: """
