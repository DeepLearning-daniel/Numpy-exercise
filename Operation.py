import numpy as np

def add(arr1, arr2):
    return arr1 + arr2

def sub(arr1, arr2):
    return arr1 - arr2

def mul(arr1, arr2):
    return arr1 * arr2

def div(arr1, arr2):
    return arr1 / arr2

def broadcast(arr, const):
    return arr * const 

if __name__ == '__main__':
    #arr1 = np.zeros(10)
    #arr2 = np.ones(10)
    arr1 = np.arange(3, 10)
    arr2 = np.arange(13, 20)
    const = 10

    res = add(arr1, arr2)
    print("Result : {}".format(res))
