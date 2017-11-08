import numpy as np
import cv2
import matplotlib.pyplot as plt
image = cv2.imread('1.jpg')
size = np.shape(image)
c = np.zeros(size)
B = image[:, :, 0]
G = image[:, :, 1]
R = image[:, :, 2]
c[:,:,0] = R[:,:] > 100
c[:,:,1] = c[:,:,0]
c[:,:,2] = c[:,:,1]
im = c*image
a = np.array([[12,3,4,4],[23,4,3,22]])
b = np.array([[0,1,1,0],[1,1,0,0]])
c = np.array([[23,3,45,3],[3,4,5,6]])
d = (a[:,:] > b[:,:]) & (a[:,:] > c[:,:])
print(a[:,:] > b[:,:])
print(a[:,:] > c[:,:])
print(d)