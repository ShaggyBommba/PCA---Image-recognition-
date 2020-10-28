import numpy as np


def img2vector(img, axis = 0):
    '''converts img to vector'''
    length = img.shape[0]*img.shape[1]
    if (axis == 0):
        return np.reshape(img, (length, 1), order="C")
    elif (axis == 1):
        return np.reshape(img, (length, 1), order="F")
    else:
        return None 

def img2gray(img):
    '''convert img to a black and white img'''
    return None