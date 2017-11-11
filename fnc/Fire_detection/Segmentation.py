"""
Author: Do Tieu Thien
Date: 06/11/1017
"""

""" Import """
from fnc.Fire_detection.HSI import HSI
from fnc.Fire_detection.RGB_model import RGB_model

""" Function """
def Segmentation(image):
    Thres_R = 140  # Threshold of Red
    # Apply RGB colour model
    im = RGB_model(image, Thres_R)
    # Convert image into HSI colour space
    im_HSI = HSI(im)
    H = im_HSI[:, :, 0]
    S = im_HSI[:, :, 1]
    I = im_HSI[:, :, 2]
    # Condition of flames pixel:
    im_HSI_temp = ((H[:, :] >= 0) & (H[:, :] <= 60)) & ((S[:, :] >= 0.3) & (S[:, :] <= 1)) & (
    (I[:, :] >= 120) & (I[:, :] <= 255))
    im_HSI[:, :, 0] = im_HSI_temp[:, :]
    im_HSI[:, :, 1] = im_HSI_temp[:, :]
    im_HSI[:, :, 2] = im_HSI_temp[:, :]
    image_1 = im_HSI * image

    return(image_1)
