# PCA---Image-recognition

## Introduction 
The purpose of this repository is to provide the reader valuable insight regarding PCA. To do this we will try to use PCA analysis to identify faces. In summary, the PCA method is a transformation of the feature space in manner that offers valuable insight related to the data. It does this by calculating a set of new basis vectors that are along direction of most change in the data. These new axises are orthogonal to each other and they are linear combinations of the original basis vectors. 

## Face recognition
The dataset used contains 7 faces, where each face contains 11 unique images. Before performing a PCA analysis each picture needs to be translated to an appropriate formatwhich the cumputer can read and perform computation upon. A picture is represented as a matrix, containing values between 0 and 255, which represent the colors. To convert this to a more approriate format each matrix related to a face is converted to a vector. Each of these vectors are merged together to form a new matrix where the vectors are represented as column vectors. 

<img src="https://latex.codecogs.com/gif.latex?I_i&space;\sim&space;(N,N)&space;\\vec(I)&space;=&space;\vec&space;\zeta&space;\sim&space;(N^{2},)&space;\\A&space;=&space;[\zeta_1,...,\zeta_M]&space;\sim&space;(N^2,M)" title="I_i \sim (N,N) \\vec(I) = \vec \zeta \sim (N^{2},) \\A = [\zeta_1,...,\zeta_M] \sim (N^2,M)" />

To determine weather an image is related with another image one must understand how each componenet of the images are related. An effective measurment which could explain how each component is related is the covariance and corellation between the components of the images. This could be done by constructing a covariance matrix. To consturct a covariance matrix from A the matrix has to be standardize. To standardize the matrix one has to calculate the average of each component. Once the matrix has been standardized the covariance matrix could be calculatad. The covariance matrix is calculated by multipltying A with its transpose. However, the size of such a matrix would be large. Therefore, the transpose of A is multiplied with itself which result in a substantially smaller matrix. Later on we will show how these two matrecies are related.  

<img src="https://latex.codecogs.com/gif.latex?\vec\mu&space;=&space;\sum_{i=1}^{M}\zeta_i&space;\\A&space;=&space;[\zeta_1,...,\zeta_M]-\vec\mu" title="\vec\mu = \sum_{i=1}^{M}\zeta_i \\A = [\zeta_1,...,\zeta_M]-\vec\mu" />
