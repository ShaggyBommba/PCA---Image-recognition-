from Model import PCA
import numpy as np
import DataProcessing as dp
import matplotlib.pyplot as plt



def test(X, Y, k, r=10, weighted=False):
    result = np.empty(r)
    for i in range(r):
        X_train, Y_train, X_test, Y_test = dp.split(X,Y,p=0.20)
        pca = PCA(X_train,Y_train)
        pca.fit()
        predictions = pca.predict(X_test,k, weighted=weighted)      

        score = (predictions == Y_test[:,0])
        score = score.sum()/len(score)
        result[i] = score
        print("Score: {}".format(score))
    return result.mean()

def plot(pca):
    pca.plot_Eigenfaces(5,5)
    pca.plot_pricipla_axis(2,2)
    pca.plot_eigenvalues()

def test_alogorithm(X, Y, r=10, weighted=False):
    result_unweighted = []
    result_weighted = [] 
    for i in range(1,r):
        print(i)
        result_unweighted.append(test(X,Y,i,weighted=False))
        result_weighted.append(test(X,Y,i,weighted=True))
    plt.plot(result_unweighted, label = "unweighted")
    plt.plot(result_weighted, label = "weighted")
    plt.legend()
    plt.show()



X,Y = dp.read_data("C:\\Users\\Jonas Meddeb\\Desktop\\Jonas Meddeb\\Datascience\\PCA---Image-recognition-\\Data\Images")
X_train, Y_train, X_test, Y_test = dp.split(X,Y,p=0.20)
test_alogorithm(X,Y)
#pca = PCA(X_train,Y_train)
#pca.fit()
#test(X,Y,5,weighted=False)
#plot(pca)







