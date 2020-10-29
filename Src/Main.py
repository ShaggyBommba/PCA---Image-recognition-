from Model import PCA
import DataProcessing as dp

print("a")
data = dp.read_data("C:\\Users\\Jonas Meddeb\\Desktop\\Jonas Meddeb\\Datascience\\PCA---Image-recognition-\\Data\Images")
print("b")
data = dp.standardization(data)
print("c")
pca = PCA(data)
print("d")
data2 = pca.fit()
print("e")
pca.plot()

