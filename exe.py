"""
Author: Do Tieu Thien
Date: 06/11/1017
"""

""" ****************************************************************************************** """
""" IMPORT """
""" ****************************************************************************************** """
import cv2
import os
from fnc.Fire_detection.Segmentation import Segmentation
from fnc.Fire_detection.Removal import Removal
import time


""" ****************************************************************************************** """
""" PROGRAM """
""" ****************************************************************************************** """
cap = cv2.VideoCapture(1)
check = True
count_1 = 0
count_2 = 0

while check:
    check, image = cap.read()

    if (count_1 % 30) == 0:
        count_2 += 1
        # Save image in Image folder
        cv2.imwrite("..\Fire_detection\Image\image%d.jpg" % count_2,image)

        # Segmentation
        img_temp = cv2.imread("Image/image%d.jpg" % count_2)
        exec("image_%d = Segmentation(img_temp)" % count_2)

        # Remove spurious flames
        if count_2 >= 2:
            exec("image_Seg_1 = image_%d" % (count_2 - 1))
            exec("image_Seg_2 = image_%d" % count_2)
            image_result = Removal(image_Seg_1, image_Seg_2)

            if sum(sum(image_result[:,:,0])) > 0:
                print("WARNING...")

    count_1 += 1

    # Remove old images
    if count_1 == 151:
        count_1 = 0
        count_2 = 0
        dirPath = "..\Fire_detection\Image"
        fileList = os.listdir(dirPath)
        for fileName in fileList:
            os.remove(dirPath + "/" + fileName)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


""" ****************************************************************************************** """
""" END """
""" ****************************************************************************************** """