import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg
## pre main opens file and creates list
fileobject = open("clouds.txt", "r")
floatlist = []
for line in fileobject:  # for each line in a file object we read line by line then split
    cs = line.split()
    dataline = [float(num) for num in cs]  # converts num for every num in cs
    floatlist.append(dataline)  # appends float values to list
data = np.array(floatlist)  #turns data to be a numPy array of floatlist

def center(data):  # center function mean subtraction
    meanofarray = np.mean(data,axis=0)
    centered = data - meanofarray
    centered = centered / np.abs(centered).max(axis=0)
    # print(meanofarray.shape) # this prints the shape of our dimensions (10)
    return centered

cent = center(data)
def covariance(k): # new function for covariance to get covar
    gram = np.dot(k.T, k) # dot product of transpose and the regular centered data
    cov = gram/k.shape[0]
    return cov

covmatrix = covariance(cent)
def Eigen(covar):
    eigenvalue, eigenvector = linalg.eig(covar)
    return eigenvalue, eigenvector

eval, evec = Eigen(covmatrix)
Z = zip(eval, evec)  # is TUPLE PAIR OF VALUE AND VECTOR
eigenvaluelist = []
eigenvectorlist = []
for n in Z:
    eigenvaluelist.append(n[0])
    eigenvectorlist.append(n[1])
#print(eigenvectorlist)
#print(eigenvaluelist)

p = (eigenvaluelist, 0.9)
def pca(D, vec, alpha): #computes variance r from PCA slides 85 chapter 3
    summation = sum(eigenvaluelist)  #sum of all r (variance)
    vectors = []
    cumlative = 0
    r = 0
    var = []
    for i in eigenvaluelist:
        cumlative += i
        r += 1
       # print(cumlative)
        total = cumlative / summation
        var.append(i)
        #print(var,"<= eigenvalue and****its total:", total)
        if(total > alpha):
           break
    var = np.array(var)
    x = slice(0, r)
    vectors = eigenvectorlist[x]
    vectors = np.array(vectors)
    return vectors
def PCA2(D, vec, alpha): #computes variance r from PCA slides 85 chapter 3
    summation = sum(eigenvaluelist)  #sum of all r (variance)
    cumlative = 0
    r = 0
    var = []
    for i in eigenvaluelist:
        cumlative += i
        r += 1
       # print(cumlative)
        total = cumlative / summation
        var.append(i)
        #print(var,"<= eigenvalue and****its total:", total)
        if(total > alpha):
           break
    var = np.array(var)
    return var
graph1 = pca(eigenvaluelist,eigenvectorlist,0.9)
graph2 = PCA2(eigenvaluelist,eigenvectorlist,0.9)
print(graph2)

def plotfunction(X,Y):
    x = X
    y = Y
    plt.ylabel("PCA")
    plt.xlabel("eigenvalue")
    plt.title("part e: graph of vector and value")
    fig = plt.scatter(x,y)
    fig.show()

from sklearn.decomposition import PCA
def sklpca(X):
        X = np.array(eigenvaluelist)
        pca = PCA(n_components=2)
        pca.fit(X)
        PCA(n_components=2)
        print(pca.explained_variance_ratio_)
        print(pca.singular_values_)
        return X
