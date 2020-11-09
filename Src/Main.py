from Model import PCA
import DataProcessing as dp



pca = PCA()
load = input("enter 1 to load data")

if(load == "1"):
    pca.load()

else:
    data = dp.read_data("C:\\Users\\Jonas Meddeb\\Desktop\\Jonas Meddeb\\Datascience\\PCA---Image-recognition-\\Data\Images")
    data = dp.standardization(data)
    data2 = pca.fit(data)
    pca.save()



