"""
Author: Do Tieu Thien
Date: 06/11/1017
"""

""" Import """
import numpy as np

""" Function """
def HSI(image):
    size = np.shape(image)
    im = np.zeros(size)
    for i in range(size[0]):
        for j in range(size[1]):
            B = image[i,j,0]
            G = image[i,j,1]
            R = image[i,j,2]
            if (R != 0) & ( G != 0) & (B != 0):
                # Convert into H array
                phi = (np.arccos(0.5*((R-G) + (R-B))/np.sqrt((R-G)*(R-G) + (R-B)*(G-B)))/np.pi)*180
                if B <= G:
                    im[i,j,0] = phi
                else:
                    im[i,j,0] = 360 - phi
                # Convert into S array
                im[i,j,1] = 1 - 3*min(R,G,B)/(R+G+B)
                # Convert into I array
                im[i,j,2] = (R+G+B)/3

    return(im)