"""
Author: Do Tieu Thien
Date: 06/11/1017
"""

""" ****************************************************************************************** """
""" IMPORT """
""" ****************************************************************************************** """
import cv2
import numpy as np
from fnc.Fire_detection.Segmentation import Segmentation
from fnc.Fire_detection.Removal import Removal
import time
start_time = time.time()


""" ****************************************************************************************** """
""" INIT """
""" ****************************************************************************************** """
image = cv2.imread('Image/1.png')
image = np.double(image) # Double type for Calculation

image_consecutive = cv2.imread('Image/2.png')
image_consecutive = np.double(image_consecutive)


""" ****************************************************************************************** """
""" FIRE DETECTION """
""" ****************************************************************************************** """
""" Segmentation for flames of image """
image_1 = Segmentation(image) # Type of image_1 is double
image_2 = Segmentation(image_consecutive)

""" Removal spurious flames """
image_flames = Removal(image_1,image_2) # image_flames have pixels of fire

print("--- %s seconds ---" % (time.time() - start_time))
image_flames = np.uint8(image_flames)
cv2.imshow('image_flames',image_flames)
cv2.waitKey(0)
cv2.destroyAllWindows()


""" ****************************************************************************************** """
""" END """
""" ****************************************************************************************** """