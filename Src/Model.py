import numpy.linalg as lin
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class PCA():
    ''' '''
    principle_axis = None
    principle_proj = None
    pcrinciple_compenent = None

    def fit(self,data):
        ''' ''' 
        print("fitting model")
        U, S, VH = lin.svd(data, full_matrices=False)
        self.pcrinciple_compenent = S
        self.principle_axis = U
        self.principle_proj = VH

    def predict(self, img):
        ''' ''' 
        pass

    def plot(self):
        index = [i for i in range(30)]
        for i in range(5):
            plt.subplot(2, 3, i+1)
            plt.bar(index, self.principle_proj[i,0:30])

        weights = self.pcrinciple_compenent.cumsum()/self.pcrinciple_compenent.sum()
        plt.subplot(2, 3, 6)
        plt.plot([i for i in range(0,len(weights))], weights)    
        plt.show()

    def save(self):
        print("Saving data")
        np.savetxt("Data/PCA/pcrinciple_compenent.csv", self.pcrinciple_compenent, delimiter=",")
        np.savetxt("Data/PCA/principle_proj.csv", self.principle_proj, delimiter=",")
        np.savetxt("Data/PCA/principle_axis.csv", self.principle_axis, delimiter=",")
    
    def load(self):
        print("Loading data")
        np.loadtxt("Data/PCA/pcrinciple_compenent.csv", self.pcrinciple_compenent, delimiter=",")
        np.loadtxt("Data/PCA/principle_proj.csv", self.principle_proj, delimiter=",")
        np.loadtxt("Data/PCA/principle_axis.csv", self.principle_axis, delimiter=",")
