import numpy as np

def RGB_model(image,Thres_R):
    size = np.shape(image)
    im_1 = np.zeros(size)
    im_2 = np.zeros(size)

    B = image[:,:,0]
    G = image[:,:,1]
    R = image[:,:,2]

    # Condition 1: R > Threshold
    im_1[:,:,0] = R[:,:] > Thres_R
    im_1[:,:,1] = im_1[:,:,0]
    im_1[:,:,2] = im_1[:,:,0]
    image = image*im_1

    # Consition 2: R>G>B
    im_2[:,:,0] = (R[:,:] > G[:,:]) & (R[:,:] > B[:,:]) & (G[:,:] > B[:,:])
    im_2[:,:,1] = im_2[:,:,0]
    im_2[:,:,2] = im_2[:,:,0]
    image = image*im_2

    return(image)



