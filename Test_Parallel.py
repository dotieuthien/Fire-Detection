"""
Author: Do Tieu Thien
Date: 06/11/1017
"""

""" IMPORT """
import cv2
import numpy as np
from fnc.Fire_detection.Segmentation import Segmentation
from fnc.Fire_detection.Removal import Removal
from fnc.Smoke_detection.Smoke_Segmentation import Smoke_Segmentation
import threading
import time

""" INIT """
# Image 1
image = cv2.imread('Image/1.png')
image = np.double(image) # Double type for Calculation
# Image 2
image_consecutive = cv2.imread('Image/2.png')
image_consecutive = np.double(image_consecutive)

""" FIRE DETECTION """
""" Segmentation for flames of image """
start_time = time.time()
# Creat threads
if __name__ == "__main__":
    image_1 = threading.Thread(target = Segmentation, args = (image,))
    image_2 = threading.Thread(target = Segmentation, args = (image_consecutive,))
    print("--- %s seconds ---" % (time.time() - start_time))
    image_1.start()
    image_2.start()
    image_1.join()
    image_2.join()
