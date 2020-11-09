import pandas as pd
from skimage import io
import os
import sys
import ImageProcessing as ip


def read_data(path):
    ''' reads images from file'''
    print("reading images from file")
    data = dict()
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
        v = ip.img2vector(img, axis=1)

        #adding to dictionary 
        data[(subject,atribute)] = v

    #creating a matrix consisting of each image as a columnvector
    df = pd.DataFrame(data) 
    return df.T

def standardization(data):
    ''' standardizing data so mean is zero '''
    mean = data.mean(axis=0)
    data = data -mean
    return data
