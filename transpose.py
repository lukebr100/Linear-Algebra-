from matrix_tests import vector_matrix_test
from print_matrix import print_matrix

def transpose(A):
    if vector_matrix_test(A)[0] == True:
        m = len(A[:])
        n = len(A[0][:])
        tA = [[A[i][j] for i in range(m)] for j in range(n)]
        return tA
A = [[1, 2], [3, 4]]
TA = transpose(A)
# print_matrix(TA)

B = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
TB = transpose(B)
# print_matrix(TB)
