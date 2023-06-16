from detect_type import detect_type
from vector_matrix_test import vector_matrix_test
from rowops import rowadd
from print_matrix import print_matrix
from rowops import rowswap


def gaussian_elim(A):
    if  vector_matrix_test(A)[0] == True and detect_type(A)[0] == True:
        m = len(A)          # store number of sublists in A (rows)
        n = len(A[0])       # store the number of columns of A
        C = [ [0 for _ in range(n)] for _ in range(m) ]      # initailizes matrix of cofactors[sic?]
        B = [row[:] for row in A]                                             # !!! NOTICE [:] !!! idk why i need it though?
        for i in range(n):              # arbitrary column       
            k = 0                       # counter
            
            for j in range(i, m - 1):   # row from i, i + 1, ..., m - 2
                
                if B[j - k][i] != 0 and B[j + 1][i] != 0:    # the pivot position is non-zero // j - k is constant in this loop   
                    t = B[j - k][i]     # store pivot
                    C[j + 1][i] = - (B[j + 1][i] / t)               # calculate factor
                    B = rowadd( B, j - k, j + 1, C[j + 1][i])       # perform row op
                    k = k + 1                                       # add to counter
                elif B[j - k][i] == 0 and B[j + 1][i] != 0:         # as of 6/16/23 handles if a pivot position is zero, swaps zero in pivot spot w/ a nonzero entry  
                    B = rowswap(B, j - k, j + 1)                    # rowswap of rows j - k and j + 1 in B
                    return gaussian_elim(B)                         # run this algorithm on the result, the new element in the pivot is non-zero!
        return B
    else:
        return "please input a matrix"
    

    


A = [[1, 2, 3],                               #works, result in REF
    [4, 5, 6], 
    [7, 8, 9]]
# tildeA = gaussian_elim( A )
# print_matrix(tildeA)

B = [[1, 2, 3, 4],                           # works
    [5, 6, 7, 8],
    [9, 10, 11, 12]]
# tildeB = (gaussian_elim( B ))
# print_matrix(tildeB)

C = [[1, 2, 3], [4, 5, 6], [7,8, 9], [10, 11, 12]]      # works
# tildeC = gaussian_elim( C )
# print_matrix(tildeC)

D = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]           # works
# tildeD = gaussian_elim( D )
# print_matrix(tildeD)

E = [[0, 0, 0], [1, 1, 1], [1, 2, 3]]           # matrix NOT in REF before 6/16/23
tildeE = gaussian_elim( E )             # WORKS, in REF! as of 6/16/23 this is due to handling the one elif: conditon using recursion  
print_matrix(E)
print_matrix(tildeE)       
           
E1 = [[1, 2, 3], [1, 1, 1], [0, 0, 0]]          # works
tildeE1 = gaussian_elim( E1 )
# print_matrix(tildeE1)

E2 = [[1, 2, 3], [0, 1, 0], [1, 0, 1]]
# print_matrix(E2)                            # prints E2
# tildeE2 = gaussian_elim( E2 )               # WORKS, in REF!
# print_matrix(E2)                            # ??? doesn't print E2 // prints tildeE2 ??? what gives? tried correct code w/ adding dummy var B = A line
# print_matrix(tildeE2)                       # same as print_matrix(E2)
                                            # the above question was answered by adding B = A[:] similarly to row from row_i.py, rowscale_1 from rowops.py! 
