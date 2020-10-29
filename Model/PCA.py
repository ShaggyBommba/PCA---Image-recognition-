import numpy.linalg as lin
import pandas as pd


class PCA():
    ''' '''
    matrix = None 
    principle_axis = None
    pcrinciple_compenent = None


    def __init__(self, data):
        ''' Constructor'''
        self.matrix = data 

    def fit(self):
        ''' ''' 
        U, S, V = lin.svd(self.matrix, full_matrices=True)



    def predict(self):
        ''' ''' 


