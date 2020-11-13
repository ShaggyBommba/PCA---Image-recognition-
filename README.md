# PCA---Image-recognition-

##Introduction 
The purpose of this repository is to provide the reader valuable insight regarding PCA. To do this we will try to use PCA analysis to identify faces. In summary, the PCA method is a transformation of the feature space in manner that offers valuable insight related to the data. It does this by calculating a set of new basis vectors that are along direction of most change in the data. These new axises are orthogonal to each other and they are linear combinations of the original basis vectors. 

## Face recognition
The dataset used contains 7 faces, where each face contains 11 unique images. Before performing a PCA analysis each picture needs to be translated to an appropriate formatwhich the cumputer can read and perform computation upon. A picture is represented as a matrix, containing values between 0 and 255, which represent the colors. To convert this to a more approriate format each matrix related to a face is converted to a vector. Each of these vectors are merged together to form a new matrix where the vectors are represented as column vectors. 

<img src="http://www.sciweavers.org/tex2img.php?eq=%5Cnoindent%0A%0A%24%20I_%7Bi%7D%20%20%5Csim%24%20%20%28nxn%29%3A%20matrix%20representing%20a%20face%0A%0A%24Vec%28I_%7Bi%7D%29%20%3D%20%20%5Ctheta_%7Bi%7D%24%20%5Csim%20%24%28n%5E%7B2%7D%2C%29%24%0A%0A%24A%20%3D%20%5B%5Ctheta_%7B0%7D%2C%5Ctheta_%7Bi%7D%2C...%2C%5Ctheta_%7Bm-1%7D%2C%5Ctheta_%7Bm%7D%5D%20%5Csim%24%20%20%28n%5E%7B2%7D%2Cm%29%20%0A&bc=White&fc=Black&im=gif&fs=18&ff=mathdesign&edit=0" align="center" border="0" alt="\noindent$ I_{i}  \sim$  (nxn): matrix representing a face$Vec(I_{i}) =  \theta_{i}$ \sim $(n^{2},)$$A = [\theta_{0},\theta_{i},...,\theta_{m-1},\theta_{m}] \sim$  (n^{2},m) " width="412" height="87" />

