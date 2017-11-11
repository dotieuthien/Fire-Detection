"""
Author: Do Tieu Thien
Date: 06/11/1017
"""
"""Import"""
import cv2
import numpy as np
from fnc.Segmentation import Segmentation
from fnc.Removal import Removal

""" Init """
image = cv2.imread('Image/1.png')
image = np.double(image) # Double type for Calculation
image_consecutive = cv2.imread('Image/2.png')
image_Consecutive = np.double(image_consecutive)
Thres_R = 140  # Threshold of Red

""" Segmentation flames for first image """
image_1 = Segmentation(image,Thres_R) # Type of image_1 is double
image_2 = Segmentation(image_consecutive,Thres_R)
im_1 = np.uint8(image_1)
im_2 = np.uint8(image_2)
cv2.imshow('image', im_1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('image', im_2)
cv2.waitKey(0)
cv2.destroyAllWindows()

""" Removal spurious flames """
Removal(image_1,image_2)

