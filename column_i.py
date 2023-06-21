from matrix_tests import test_VectNum, test_MatrixVect
# function, input: A matrix column to access
# output: ith column of A
def column(A, i):
    if test_VectNum(A)[0] == True:
        return [A[i]]
    if test_MatrixVect(A) == True and i < len(A[0]):
        return [row[i] for row in A]
    else:
        return False