from matrix_tests import test_VectNum, test_MatrixVect
def row(A, i):
    B = A.copy()
    if test_VectNum(B)[0] == True and i == 0:
        return B[:]
    elif test_MatrixVect(B) == True and i < len(B[:]):
        return B[i][:]
    else:
        return False

