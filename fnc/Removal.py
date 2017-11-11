import numpy as np
import cv2
from fnc.Segmentation import Segmentation

def Removal(image1, image2):
    # Convert background of image 1 into blue
    im1 = (image1[:,:,2] == 0)
    im1 = im1*255
    image1[:,:,0] = image1[:,:,0] + im1[:,:]
    image1[:,:,1] = image1[:,:,1] + im1[:,:]
    # Convert background of image 2 into blue
    im2 = (image2[:,:,2] == 0)
    im2 = im2*255
    image2[:,:,0] = image[:,:,0] + im2[:,:]
    image2[:,:,1] = image[:,:,1] + im2[:,:]
    # Remove spurious flames
    image_sub = np.abs(image1 - image2)
    im = np.uint8(image_sub)
    cv2.imshow('image', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return(image_difference)
