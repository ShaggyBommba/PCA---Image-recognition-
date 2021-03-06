# PCA---Image-recognition

## Introduction 
The purpose of this repository is to provide the reader valuable insight regarding PCA. To do this we will try to use PCA analysis to identify faces. In summary, the PCA method is a transformation of the feature space in manner that offers valuable insight related to the data. It does this by calculating a set of new basis vectors that are along direction of most change in the data. These new axises are orthogonal to each other and they are linear combinations of the original basis vectors. 

## Face recognition
The dataset used contains 7 faces, where each face contains 11 unique images. Before performing a PCA analysis each picture needs to be translated to an appropriate formatwhich the cumputer can read and perform computation upon. A picture is represented as a matrix, containing values between 0 and 255, which represent the colors. To convert this to a more approriate format each matrix related to a face is converted to a vector. Each of these vectors are merged together to form a new matrix where the vectors are represented as column vectors. 

<img src="https://latex.codecogs.com/gif.latex?I_i&space;\sim&space;(N,N)&space;\\vec(I)&space;=&space;\vec&space;\zeta&space;\sim&space;(N^{2},)&space;\\A&space;=&space;[\zeta_1,...,\zeta_M]&space;\sim&space;(N^2,M)" title="I_i \sim (N,N) \\vec(I) = \vec \zeta \sim (N^{2},) \\A = [\zeta_1,...,\zeta_M] \sim (N^2,M)" />

To determine weather an image is related with another image one must understand how each componenet of the images are related. An effective measurment which could explain how each component is related is the covariance and corellation between the components of the images. This could be done by constructing a covariance matrix. To consturct a covariance matrix from A the matrix has to be standardize. To standardize the matrix one has to calculate the average of each component. The vectors obtained by taking the average of the component from  each face represents the average face. The average face calculated from the dataset in the repository result in the following face:

![Image of average face](https://github.com/ShaggyBommba/PCA---Image-recognition-/blob/main/Output/Mean_face.png)

Once the matrix has been standardized the covariance matrix could be calculatad. The covariance matrix is calculated by multipltying A with its transpose. However, the size of such a matrix would be large. Therefore, the transpose of A is multiplied with itself which result in a substantially smaller matrix. Later on we will show how these two matrecies are related.  

<img src="https://latex.codecogs.com/gif.latex?\vec\mu&space;=&space;\sum_{i=1}^{M}\zeta_i&space;\\A&space;=&space;[\zeta_1,...,\zeta_M]-\vec\mu&space;\\C&space;=&space;A^TA&space;\sim&space;(M,M)" title="\vec\mu = \sum_{i=1}^{M}\zeta_i \\A = [\zeta_1,...,\zeta_M]-\vec\mu \\C = A^TA \sim (M,M)" />

A is a diagonalizable matrix as it is square. Therefore, we can calculate its eigenvalues and eigenvectors. By calculating those we can identify a new set of basis vectors. Moreover, as each eigenvector has an associated eigenvalue, the importance of each axis can be quantified systematically. However, these eigenvectors and eigenvalues are associated with the covariance between images, not between the components each image comprises of. To obtain those eigenvectors, one needs to calculate the eigenvalues for the aforementioned larger matrix. However, by multiplying the eigenvalues obtained from C with matrix A the eigenvalues of interest are obtained.

<img src="https://latex.codecogs.com/gif.latex?\noindent&space;\\\vec&space;u,&space;\vec&space;\lambda&space;=&space;eig(A^TA)&space;\\A^TA&space;\vec&space;u&space;=\vec&space;\lambda&space;\vec&space;u&space;\\AA^TA&space;\vec&space;u&space;=\vec&space;\lambda&space;A&space;\vec&space;u&space;\\AA^T(A&space;\vec&space;u)&space;=&space;\vec&space;\lambda&space;(A&space;\vec&space;u)" title="\noindent \\\vec u, \vec \lambda = eig(A^TA) \\A^TA \vec u =\vec \lambda \vec u \\AA^TA \vec u =\vec \lambda A \vec u \\AA^T(A \vec u) = \vec \lambda (A \vec u)" />

These eigenvector represents the faces which each face consist of. In layman terms these eigenvectors are referred to as eigenfaces. The eigenfaces obtained from this dataset are presented below: 

![Eigenfaces](https://github.com/ShaggyBommba/PCA---Image-recognition-/blob/main/Output/Eigenfaces.png)

However, how could the be used to predict the face of a person. Well by transforming the face to the new vector space we can analyze the closeness to other faces by using well established methods such as KNN.


## Result
