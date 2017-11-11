"""
Author: Do Tieu Thien
Date: 06/11/1017
"""

""" Import """
from fnc.HSI import HSI

""" Function """
def Pos_Segmentation(image):
    # Convert image into HSI colour space
    im_HSI = HSI(image)
    H = im_HSI[:, :, 0]
    S = im_HSI[:, :, 1]
    I = im_HSI[:, :, 2]
    # Condition of flames pixel:
    im_HSI_temp = ((H[:, :] >= 0) & (H[:, :] <= 60)) & ((S[:, :] >= 0.2) & (S[:, :] <= 1)) & (
    (I[:, :] >= 100) & (I[:, :] <= 255))
    im_HSI[:, :, 0] = im_HSI_temp[:, :]
    im_HSI[:, :, 1] = im_HSI_temp[:, :]
    im_HSI[:, :, 2] = im_HSI_temp[:, :]
    image_1 = im_HSI * image

    return(image_1)
