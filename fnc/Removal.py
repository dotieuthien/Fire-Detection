import numpy as np
import cv2
from fnc.Pos_Segmentation import Pos_Segmentation

def Removal(image1, image2):
    # Convert background of image 1 into blue
    im1 = (image1[:,:,2] == 0)
    im1 = im1*255
    image1[:,:,0] = image1[:,:,0] + im1[:,:]
    imshow1 = np.uint8(image1)
    cv2.imshow('image', imshow1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Convert background of image 2 into blue
    im2 = (image2[:,:,2] == 0)
    im2 = im2*255
    image2[:,:,0] = image2[:,:,0] + im2[:,:]
    imshow2 = np.uint8(image2)
    cv2.imshow('image', imshow2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Remove spurious flames
    image_sub = np.abs(image1 - image2)
    image_sub = Pos_Segmentation(image_sub)
    im = np.uint8(image_sub)
    cv2.imshow('image', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return(image_sub)
