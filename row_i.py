from matrix_tests import vector_matrix_test
def row(A, i):
    B = A
    if 'row vector' in vector_matrix_test(B)[1] and i == 0:
        t = B[:]
        return t
    elif 'matrix' in vector_matrix_test(B)[1]:
        t = B[i][:]
        return t
    elif 'column vector' in vector_matrix_test(B)[1]:
        t = [B[i]]
        return t
    else:
        return B, 'is not a matrix'

A = [[1, 2], 
     [3, 4]]    
# print(row(A, 1))                    # first sublist of A

RowA = [_ for _ in range(5)]
# print(RowA)
# print(row(RowA, 0))
