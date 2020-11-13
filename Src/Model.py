import numpy.linalg as lin
from collections import Counter
import numpy as np
import DataProcessing as dp
import pandas as pd
import matplotlib.pyplot as plt


class PCA():
    ''' '''
    KNN_model = None
    Y = None
    X = None
    X_proj = None
    principle_axis = None
    pcrinciple_compenent = None


    def __init__(self,data,label):
        self.Y = label
        self.X = data



    def fit(self):
        ''' ''' 
        print("fitting model")
        X = dp.standardization(self.X)
        C = X.dot(X.T)
        S,W = lin.eigh(C)

        index = S.argsort()[::-1]
        self.pcrinciple_compenent = S[index]
        self.principle_axis = W[:,index]

        self.X_proj = np.dot(np.transpose(X), self.principle_axis)

        #normalizing vectors
        for idx,v in enumerate(self.X_proj.T):
            self.X_proj[:,idx] = self.X_proj[:,idx] / lin.norm(v)
        


        self.KNN_model = KNN(self.principle_axis, self.Y, self.X_proj)


    def predict(self, images, k, weighted = False):
        ''' ''' 
        predictons = []
        for image in images:
            if(weighted):   pred = self.KNN_model.KNN_weighted(image,k)
            else:   pred = self.KNN_model.KNN_unweighted(image,k)
            predictons.append(pred)
        return np.array(predictons)


    def plot_Eigenfaces(self, row, col):
        col = int(col)
        row = int(row)
        numbeer_pictures = int(row*col)


        for i in range(numbeer_pictures):
            plt.subplot(row, col, i+1)
            v = self.X_proj[:,i].copy()
            shape = (243,320)
            v.resize(shape)
            plt.imshow(v, cmap='gray')
            plt.title("Eigenface_{}".format(i+1))
        
        plt.show()

    def plot_pricipla_axis(self, row, col):
        lables = np.unique(self.Y[:,0], return_inverse=True)[1]
        for i in range(row*col):
             plt.subplot(row, col, i+1)
             plt.scatter(x = self.principle_axis[:,i], y = self.principle_axis[:,(i+1)], c=lables)
             plt.title("Pcrinciple Axis: P{} & P{}".format(i,i+1))
             plt.xlabel("P{}".format(i))
             plt.ylabel("P{}".format(i+1))
        plt.show()
    
    def plot_eigenvalues(self):
        cum = np.cumsum(self.pcrinciple_compenent)/np.sum(self.pcrinciple_compenent)
        plt.plot(cum)
        plt.title("Cumulative sum of eigenvalues")
        plt.xlabel("number of axis")
        plt.ylabel("Variance covered")
        plt.show()

             


class KNN():

    Feature_space = None
    principle_axis = None
    Y = None 

    def __init__(self, principle_axis, Y, Feature_space):
        self.Feature_space = Feature_space
        self.principle_axis=principle_axis
        self.Y=Y

    def KNN_unweighted(self, v, k):
        v0 = (v.T).dot(self.Feature_space)
        k = [(" ",float("inf")) for i in range(k)]

        for (label,image) in enumerate(self.principle_axis):
            dist = lin.norm(v0-image)

            for idx,p in enumerate(k):
                if dist < p[1]:
                    k[idx] = ( self.Y[:,0][label], dist )
                    break

            k = sorted(k, key = lambda x : x[1], reverse=True)
        k = Counter([e[0] for e in k]).most_common(1)[0][0]
        return k

    def KNN_weighted(self, v, k):
        v0 = (v.T).dot(self.Feature_space)
        k = [(" ",float("inf")) for i in range(k)]

        for (label,image) in enumerate(self.principle_axis):
            dist = lin.norm(v0-image)

            for idx,p in enumerate(k):
                if dist < p[1]:
                    k[idx] = ( self.Y[:,0][label], dist )
                    break

            k = sorted(k, key = lambda x : x[1], reverse=True)
        
        score = dict()

        for e in k:
            subject = e[0]
            vote = 1/e[1]
            if e[0] in score:
                score[subject] = score[subject] + vote
            else:
                score[subject] = vote

        Keymax = max(score, key=score.get)

        return Keymax



