from matrix_tests import vector_matrix_test
# function, input: A matrix column to access
# output: ith column of A
def column(A, i):
    if 'row vector' in vector_matrix_test(A)[1]:                                        # input matrix is row vector
        return [A[i]]
    elif 'column vector' in vector_matrix_test(A)[1]:                                   # input is column vector
         return [sublist[0] for sublist in A]
    elif 'matrix' in vector_matrix_test(A)[1]:                                 # input is matrix               
        return [sublist[i] for sublist in A]            # output the ith entry of each sublist
    else:
        return 'not a matrix'


A = [[1, 2], [3, 4]]    
# print(column(A, 0))   
