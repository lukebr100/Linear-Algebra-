from matrix_tests import vecnum_test, vector_matrix_test

def dot_product(x, y):
    # function (dot/scalar product): input number vectors x, y
    # output: scalar given by Euclidean inner product
    a = len(x)
    # store length of x into var a
    z = 0
    # set counter
    if vecnum_test(x) == True and vecnum_test(y) == True and a == len(y):
        # if both x, y pass vecnum_test and length of x == length of y
        for i in range(a):
            # for i ranging over all indices of x, y
            z = z + x[i] * y[i]
            # overwrite z w/ trhe previous value of z and the product of x[i], y[i]
        return z
        # after the loop, return z, x[i]*y[i] for all i
    else:
        return 'need equal length vectors'
        # dimension of vectors needs to be the same 
    

def matrix_mult(A, B):
    # matrix multiplcation
    if vector_matrix_test(A)[0] == True and vector_matrix_test(B)[0] == True:
        mA = len(A[:])
        # rows of A
        nA = len(A[0][:])
        # cols of A
        
        mB = len(B[:])
        # rows of B
        nB = len(B[0][:])
        # cols of B
        
        if nA == mB: # cols of A == rows of B (compatible)
            C = [[0 for k in range(nB)] for l in range(mA)]
            # intialize product C w/ rows of A and cols of B
            
            for i in range(mA):
                # row of A
                for j in range(nB):
                    # col of B
                    A_rowi = row(A, i)
                    # store row i of A into var A_rowi
                    B_colj = column(B, j)
                    # store col j of B into var B_colj
                    C[i][j] = dot_product(A_rowi, B_colj)
                    # the ith row, jth col of C is given by the dot product of A_rowi, B_colj
            return C
            # after nest for loops, print matrix C
        else:
            return 'incompatible matrices'
            # number of cols of A == number of rows of B 

A = [[1, 1], [0, 1]]
# define matrix A
B = [[1, 2], [3, 4]]
# define matrix B
# print(matrix_mult(A, B))
# ther product
