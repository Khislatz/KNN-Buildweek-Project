# KNN-Buildweek-Project-

In this project I tried to develop a K-Nearest Neighbors Algorithm from scratch without using scikit-learn KNeighborsClassifier and test it on a real world dataset. Dataset "Census Income Data Set" was borrowed from UCI library. Then compared my results with the scikit-learn KNN results. The results of this dataset can be found in the "main_KNN_project" folder. I also tested my algorithm on a famous Titanic dataset. The results can be found in "titanic_KNN_testing" folder. 


What is KNN?
KNN is a supervised machine learning algorithm that can be used for both classification and regression problems. However, it is mainly used to solve classification problems. In classification problems, the output is a class, which is defined by the majority votes of k neighbors.

What is "k"?
k in KNN is the parameter that defines the number of nearest neighbors, the majority votes of which decides the output.
There is no particular way to determine the optimal value of k that would lead to a better accuracy. Most of the time, we need to use a trial and error method.

Pseudocode for KNN algorithm:
    - Create a constructor method that will take a k value.
    - Create fit method, which will store our training data that we will use later on.
    - Create a predict method, which will consist of two functions, one of which will be used as a helper function and another one as a main function.
    - In a helper function 1) we will need to calculate distances between a new point and its nearest neighbors; 2) obtain the labels of the k nearest neighbors; 3) find the most common class that will decide which class the new point belongs to; 4) return the most common class.
To calculate distances between a new point and its neighbors, we will create two functions: euclidean_d and manhattan_d, which could be equally utilized. However, the most commonly used method to calculate distances is Euclidian distance.


Additional information can be found at: https://khislatz.medium.com/how-to-write-a-k-nearest-neighbors-algorithm-and-apply-it-on-a-real-world-dataset-7322d96dac66