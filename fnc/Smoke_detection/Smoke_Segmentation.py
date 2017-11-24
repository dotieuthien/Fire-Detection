"""
Author: Do Tieu Thien
Date: 15/11/1017
"""

""" Import """
import numpy  as np
import cv2

""" Function """
def Smoke_Segmentation(image):
    size = np.shape(image)
    im_mask = np.zeros(size)

    # Condition 1 for foreground of smoke
    im_max = image.max(2)
    im_min = image.min(2)
    im_1 = im_max[:,:] - im_min[:,:]

    im_1[:,:] = (im_1[:,:] < 20)
    
    im_mask[:, :, 0] = im_1[:,:]
    im_mask[:, :, 1] = im_1[:,:]
    im_mask[:, :, 2] = im_1[:,:]
    image_result = im_mask*image

    img = np.uint8(im_1)
    cv2.imshow('image_flame', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Condition 2 for foreground of smoke
    B = image_result[:, :, 0]
    G = image_result[:, :, 1]
    R = image_result[:, :, 2]

    I = (R[:,:] + G[:,:] + B[:,:])/3
    I[:,:] = ((80 <= I[:,:]) & (I[:,:] <= 150)) | ((190 <= I[:,:]) & (I[:,:] <= 220))

    im_mask[:,:,0] = I[:,:]
    im_mask[:,:,1] = I[:,:]
    im_mask[:,:,2] = I[:,:]
    image_result = im_mask*image

    return(image_result)

