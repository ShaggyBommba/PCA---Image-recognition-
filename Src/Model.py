import numpy.linalg as lin
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class PCA():
    ''' '''
    matrix = None 
    principle_axis = None
    pcrinciple_compenent = None


    def __init__(self, data):
        ''' Constructor'''
        self.matrix = data.values

    def fit(self):
        ''' ''' 
        U, S, VH = lin.svd(self.matrix, full_matrices=False)
        self.pcrinciple_compenent = U*S
        self.principle_axis = VH
        self.matrix = self.matrix * VH
        return self.matrix

    def predict(self):
        ''' ''' 
        pass

    def plot(self):
        weights = np.diagonal(self.pcrinciple_compenent)
        tot_weights = weights.sum()
        weights = weights.cumsum()/tot_weights

        plt.plot([i for i in range(0,len(weights))], weights)
        plt.show()


