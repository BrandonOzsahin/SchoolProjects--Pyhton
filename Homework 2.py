import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg
from collections import Counter


def entropy(pmf):
    result = 0.0
    for p in pmf:
        result += np.log2(p) * p
    result *= -1
    return result


def splitf(D, col, value):
    Dy = []
    Dn = []
    counter = 0
    for line in range(len(D[0])):
        counter += 1
        print(D[0][:, col])
        print(counter)

        if col <= value:

            for i in range(len(D[0])):
                # print(D[0][i], "***", D[1][i])
                Dy.append([D[0][i], D[1][i]])
            # print(Dy[4])


        else:

            for i in range(len(D[0])):
                Dn.append([D[0][i], D[1][i]])
            # print(Dn[0])
    '''print(type(D))
    print(type(Dy))
    print(Dy)
    print(Dn)
    '''
    return Dy, Dn


def IG(D, index, value):
    return 0

    """Compute the Information Gain of a split on attribute index at value
    for dataset D.

    Args:
        D: a dataset, tuple (X, y) where X is the data, y the classes
        index: the index of the attribute (column of X) to split on
        value: value of the attribute at index to split at

    Returns:
        The value of the Information Gain for the given split
    """


def G(D, index, value):
    """Compute the Gini index of a split on attribute index at value
    for dataset D.

    Args:
        D: a dataset, tuple (X, y) where X is the data, y the classes
        index: the index of the attribute (column of X) to split on
        value: value of the attribute at index to split at

    Returns:
        The value of the Gini index for the given split
    """


def CART(D, index, value):
    """Compute the CART measure of a split on attribute index at value
    for dataset D.

    Args:
        D: a dataset, tuple (X, y) where X is the data, y the classes
        index: the index of the attribute (column of X) to split on
        value: value of the attribute at index to split at

    Returns:
        The value of the CART measure for the given split
    """


def bestSplit(D, criterion):
    """Computes the best split for dataset D using the specified criterion

    Args:
        D: A dataset, tuple (X, y) where X is the data, y the classes
        criterion: one of "IG", "GINI", "CART"

    Returns:
        A tuple (i, value) where i is the index of the attribute to split at value
    """


# functions are first class objects in python, so let's refer to our desired criterion by a single name


def load(filename):
    fileobject = open(filename, "r")
    plist = []
    for line in fileobject:  # for each line in a file object we read line by line then split
        cs = line.strip("\n").split(",")
        data = [float(num) for num in cs]  # rememberfloat
        plist.append(data)
    datalist = np.array(plist)
    # print(datalist.shape)
    X = datalist[:, 0:10]
    Y = datalist[:, 10]  # rid eleventh column
    # print(Y)
    result = (X, Y)
    # print(result[1])
    return result


def createPMF(Y):
    counter = 0
    counter2 = 0
    for i in Y:
        if i == 0:  # turn counter and counter 2 into Anumpty array with both of them in it and then divide by number of elements in arg (Y)
            counter += 1
        elif i == 1:
            counter2 += 1
    result = np.array([counter, counter2]) / len(Y)
    # print (result)
    # print("amound of 1's:",counter2,"amount of 0's",counter)
    return result


def classifyIG(train, test):
    """Builds a single-split decision tree using the Information Gain criterion
    and dataset train, and returns a list of predicted classes for dataset test

    Args:
        train: a tuple (X, y), where X is the data, y the classes
        test: the test set, same format as train

    Returns:
        A list of predicted classes for observations in test (in order)
    """


def classifyG(train, test):
    """Builds a single-split decision tree using the GINI criterion
    and dataset train, and returns a list of predicted classes for dataset test

    Args:
        train: a tuple (X, y), where X is the data, y the classes
        test: the test set, same format as train

    Returns:
        A list of predicted classes for observations in test (in order)
    """


def classifyCART(train, test):
    """Builds a single-split decision tree using the CART criterion
    and dataset train, and returns a list of predicted classes for dataset test

    Args:
        train: a tuple (X, y), where X is the data, y the classes
        test: the test set, same format as train

    Returns:
        A list of predicted classes for observations in test (in order)
    """


def main():
    # load("test.txt")
    X, Y = load("test.txt")
    result = load("test.txt")
    pmf = createPMF(Y)
    S = splitf(result, 0, 1)
    e = entropy(pmf)
    #  ig = IG(result, 0, 4)
    # print(result)
    # print(pmf)
    # print(e)

    """This portion of the program will run when run only when main() is called.
    This is good practice in python, which doesn't have a general entry point
    unlike C, Java, etc.
    This way, when you <import HW2>, no code is run - only the functions you
    explicitly call.
    """


if __name__ == "__main__":
    """__name__=="__main__" when the python script is run directly, not when it 
    is imported. When this program is run from the command line (or an IDE), the 
    following will happen; if you <import HW2>, nothing happens unless you call
    a function.
    """
    main()
