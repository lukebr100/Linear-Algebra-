from matrix_tests import detect_type, vector_matrix_test
from rowops import rowadd, rowswap
from print_matrix import print_matrix
from row_i import row

def gaussian_elim(A, b):
    m = len(A)
    # store number of rows
    if  vector_matrix_test(A)[0] == True and len(b) == m:
        n = len(A[0])
        # store the number of columns of A
        C = [ [0 for _ in range(n)] for _ in range(m) ]
        # initailizes matrix of cofactors[sic?]
        B = [row(A, i) for i in range(m)]
        for i in range(n):
            # arbitrary column       
            k = 0
            # counter
            
            for j in range(i, m - 1):
                # row from i, i + 1, ..., m - 2
                
                if B[j - k][i] != 0 and B[j + 1][i] != 0:
                    # the pivot position is non-zero // j - k is constant in this loop   
                    t = B[j - k][i]
                    # store pivot
                    C[j + 1][i] = - (B[j + 1][i] / t)
                    # calculate factor
                    b[j + 1] = C[j + 1][i] * b[j - k] + b[j + 1]
                    B = rowadd( B, j - k, j + 1, C[j + 1][i])
                    # perform row op
                    k = k + 1
                    # add to counter
                elif B[j - k][i] == 0 and B[j + 1][i] != 0:
                    #  handles if a pivot position is zero, swaps zero in pivot spot w/ a nonzero entry  
                    B = rowswap(B, j - k, j + 1)
                    s = b[j - k]
                    b[j - k] = b[j + 1]
                    b[j + 1] = s
                    # rowswap of rows j - k and j + 1 in B
                    return gaussian_elim(B, b)
                    # run this algorithm on the result, the new element in the pivot is non-zero!
        return B, b
    else:
        return False

def ge_incon_ID(A, b):
    tildeA = gaussian_elim(A, b)
    # call GE function, output REF version of A, corresponding b
    n = len(A[0])
    # number of columns
    m = len(A[:])
    # number of rows 
    Zrow = [j for j in range(m) if tildeA[0][j] == [0 for i in range(n)]]
    # identifies rows of zeros in tildeA[0](REF of A), return indexes where these occur
    for k in Zrow:
        # for all zero rows
        if b[k] != 0:
            # b at that index is non-zero
            # but LHS is zero, ie, 0*x + 0*y + 0*z = 2
            # inconsistent, return GE of Ax = b
            return 'inconsistent', tildeA
    return 'consistent', tildeA
    # consistent system, return GE of Ax = b

A = [[1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]]
b = [10, 11, 12]
tildeA = ge_incon_ID( A, b )
print(tildeA[0])
print_matrix(tildeA[1])

B = [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]
# tildeB = (gaussian_elim( B ))
# print_matrix(tildeB)

C = [[1, 2, 3], [4, 5, 6], [7,8, 9], [10, 11, 12]]
# tildeC = gaussian_elim( C )
# print_matrix(tildeC)

D = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]
# tildeD = gaussian_elim( D )
# print_matrix(tildeD)

E = [[0, 0, 0], [1, 1, 1], [1, 2, 3]]
b = [4, 5, 2]
tildeE = ge_incon_ID( E, b )
print(tildeE[0])   
print_matrix(tildeE[1])
           
E1 = [[1, 2, 3], [1, 1, 1], [0, 0, 0]]
tildeE1 = ge_incon_ID( E1 , b)
print(tildeE1[0])
print_matrix(tildeE1[1])

E2 = [[1, 2, 3], [0, 1, 0], [1, 0, 1]]
# print_matrix(E2)
# tildeE2 = gaussian_elim( E2 )
# print_matrix(E2)
# # print_matrix(tildeE2)
