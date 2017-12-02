"""
Author: Do Tieu Thien
Date: 10/11/1017
"""

import numpy as np
import cv2
from fnc.Fire_detection.Pos_Segmentation import Pos_Segmentation

def Removal(image1, image2):
    # Convert background of image 1 into blue
    im1 = (image1[:,:,2] == 0)
    im1 = im1*255
    image1[:,:,0] = image1[:,:,0] + im1[:,:]

    # Convert background of image 2 into blue
    im2 = (image2[:,:,2] == 0)
    im2 = im2*255
    image2[:,:,0] = image2[:,:,0] + im2[:,:]

    # Remove spurious flames
    image_sub = np.abs(image1 - image2)
    image_sub = Pos_Segmentation(image_sub)

    return(image_sub)
