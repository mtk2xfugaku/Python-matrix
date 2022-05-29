"""
Author  : mtk2xfugaku
Summary : matrix arithmetics using only Python list.
Date    : 01-08-21
"""
def equality(A: list,B: list,tol: int =None)-> bool:
  
    """
    Check if two matrices are equal.

    tol is tolerance for floating point accuracy.

    """

    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False
    for i in range(len(A)):
        for j in range(len(A[0])):
            if tol == None:
                if A[i][j] != B[i][j]:
                    return False
                else:
                    if round(A[i][j],tol) != round(B[i][j],tol):
                        return False
    return True



def zeros(nRow: int,nCol: int)->list:
    return [[0.0 for _ in range(nCol)] for _ in range(nRow)]


def copyMat(A: list)->list:
    """
    newMat = zeros(len(A),len(A[0]))
    for i in range(len(A)):
        for j in range(len(A[0])):
            newMat[i][j] = A[i][j]
    return newMat
    """
    return A.copy()

def identityMat(n: int)-> list:
    """
    identity matrix 
    """
    mat: list = zeros(n,n)
    for i in range(n):
        mat[i][i] = 1.0
    return mat

def AddScalar(A: list,scalar)-> list:
    C : list = zeros(len(A[0]),len(A))

    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j] + scalar
    return C

def SubScalar(A: list,scalar)-> list:
    C : list = zeros(len(A[0]),len(A))

    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j] - scalar
    return C

def MulScalar(A : list,scalar) -> list:
    """matrix multiplication """
    C : list = zeros(len(A[0]),len(A))

    for i in range(len(C)):
        for j in range(len(C[0])):
                C[i][j] =  A[i][j] * scalar
    return C

def ADD(A : list,B : list) -> list:
    """
    matrix addition 
    component wise using standard formula
    """
    C : list = zeros(len(A[0]),len(A))

    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j] + B[i][j]
    return C

def SUB(A : list,B : list) -> list:
    """matrix subtraction"""
    assert len(A[0])==len(B[0]),"must be a square matrix"
    assert len(A)==len(B),"must be a square matrix"
    
    C : list = zeros(len(A[0]),len(A))

    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j] - B[i][j]
    return C

def MUL(A : list,B : list) -> list:
    """
    Arguments ::
    1. A : multidimensional list of lists
    2. B : multidimesnional list of lists
    Function :: 
    Multiplication operation on two 2 dimensional
    matrices using naive algorithm i.e 
    
    C[i][j] = A[i][k] * B[k][i]

    """
    # make an empty matrix to store the result.
    nRow : int = len(A)
    nCol : int = len(B[0])

    C : list = [[0.0 for _ in range(nCol)] for _ in range(nRow)]

    # matrix multiplication
    for i in range(nRow):
        for j in range(nCol):
            for k in range(len(A[0])):
                C[i][j] = A[i][k] * B[k][j]
    return C


def Transpose(A : list) -> list:
    """Transpose of a matrix nxm """
    C : list = zeros(len(A[0]),len(A))

    for i in range(len(A)):
        for j in range(len(A[0])):
            C[j][i] = A[i][j]
    return C

def show(A: list,decimals: int =3)-> None:
    for row in A:
        print([round(x,decimals) + 0 for x in row])
        


def display_1(A : list) -> None:
    for i in A:
        print("{}".format(i))

def display_2(A : list) -> None:
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j],end="\t")
        print("\n")

def skew(A : list) -> bool:
    """if skew symmetric then true else false"""
    for i in range(len(A)):
        for j in range(len(A[0])):
            if(A[i][j] != -(A[j][i])):
                return False
    return True
    

def symmetric(A : list) -> bool:
    """if symmetric then true else false """
    for i in range(len(A)):
        for j in range(len(A[0])):
            if(A[i][j] != A[i][j]):
                return False
    return True


def kahanNeumaierSum(Array):
    if len(Array) == 0:
        raise IndexError("Empty list passed as argument !")
    """
    Improved Kahan-Babuska summation by 
    Neumaier for accurate floating point
    summation.
    """
    sums : float = 0.0
    c    : float = 0.0

    for i in range(len(Array)):
        t : float = sums + Array[i]
        if abs(sums) >= abs(Array[i]):
            c += (sums - t) + Array[i]
        else:
            c += (Array[i] - t) + sums
        sums = t
    return sums + c


def dot(A:list,B:list)-> float:
    """
    normal summation can suffer from catastrophic
    cancellation so fsum() is used here.
    it's more accurate for FPN than sum()

    Update : I am now using KahanNumeirSum that I 
             wrote to calculate accurate floating 
             point sum.
    """
    assert len(A)==len(B),"inconsistent size of list !"

    C : list = [0 for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B)):
            C[i] = A[i]*B[i] # store the product in C.
            break
    return kahanNeumaierSum(C) # sum the C list.



def make(nRow:int,nCol:int,Real:float)-> list:
    # to make an arbitrary dimension matrix 

    C : list = [[float(Real) for _ in range(nCol)] for _ in range(nRow)]
    return C
    
def dim(L:list)->tuple:
    # get the dimension of any matrix nxm.
    return (len(L),len(L[0]))

def Type(Mat: list):
    
    return type(Mat[0][0])


def randomMat(dim1: int,dim2: int)-> list:
    """ generate a random matrix of size dim1 X dim2 """
    from random import random 
    return [[random() for _ in range(dim1)] for _ in range(dim2)]


