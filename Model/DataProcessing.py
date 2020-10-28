import pandas as pd
from skimage import io
import os
import ImageProcessing as ip


def read_data(path):
    ''' reads images from file'''

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

        print(v)
    return None

read_data("..\Data\Images")