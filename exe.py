"""
Author: Do Tieu Thien
Date: 06/11/1017
"""
"""Import"""
import cv2
import numpy as np
from fnc.Fire_detection.Segmentation import Segmentation
from fnc.Fire_detection.Removal import Removal

""" Init """
image = cv2.imread('Image/5.png')
image = np.double(image) # Double type for Calculation
image_consecutive = cv2.imread('Image/6.png')
image_Consecutive = np.double(image_consecutive)

""" FIRE DETECTION"""

""" Segmentation flames for first image """
image_1 = Segmentation(image) # Type of image_1 is double
image_2 = Segmentation(image_consecutive)

""" Removal spurious flames """
image_flames = Removal(image_1,image_2)

""" SMOKE DETECTION """
