from typing import Tuple
import numpy as np
import random
from skimage import io
import os
import sys
import ImageProcessing as ip


def read_data(path):
    ''' reads images from file'''
    print("reading images from file")
    X = []
    Y = []

    for file in os.listdir(path):

        #Identify subject and image detail
        name = file.split(".")
        subject = name[0]
        atribute = name[1]


        #Specifying path
        file_path = os.path.join(path,file)

        #Reading image
        img = io.imread(file_path, as_gray=True)

        #Creating a vector
        v = ip.img2vector(img, axis=0)

        #adding to X and Y 
        X.append(v)
        Y.append((subject,atribute))

    #creating a matrix consisting of each image as a columnvector
    X = np.array(X)
    Y = np.array(Y)

    return X,Y


def split(X, Y, p=0.20, seed=None):
    random.seed(seed)

    idx_train = []
    idx_test = []

    bins = np.split([ i for i in range(len(Y[:,0] )) ], np.unique(Y[:,0], return_index=True)[1][1:])
    for bin in bins:
        random.shuffle(bin)
        n = int( p * len(bin) )
        idx_test = idx_test + list(bin[:n])
        idx_train = idx_train + list(bin[n:])


    return X[idx_train,:], Y[idx_train,:], X[idx_test,:], Y[idx_test,:]


def standardization(data):
    ''' standardizing data so mean is zero '''
    mean = data.mean(axis=0,keepdims=True)
    data = data -mean
    print(data[:,0].mean())
    return data, mean.astype(int)
