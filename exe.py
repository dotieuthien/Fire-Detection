"""
Author: Do Tieu Thien
Date: 06/11/1017
"""

""" IMPORT """
import cv2
import numpy as np
from fnc.Fire_detection.Segmentation import Segmentation
from fnc.Fire_detection.Removal import Removal
import time
start = time.time()
""" INIT """
image = cv2.imread('Image/3.png')
image = np.double(image) # Double type for Calculation
image_consecutive = cv2.imread('Image/4.png')
image_Consecutive = np.double(image_consecutive)

""" FIRE DETECTION """
""" Segmentation flames for image """
image_1 = Segmentation(image) # Type of image_1 is double
image_2 = Segmentation(image_consecutive)

""" Removal spurious flames """
image_flames = Removal(image_1,image_2)
print(time.time() - start)
img = np.uint8(image_flames)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

""" SMOKE DETECTION """
""" Segmentation smoke region """