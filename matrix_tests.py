def detect_type(L):
    for i in range(len(L)):                                                     # every sublist of L                                            
        for j in range(len(L[i])):                                                   # for j spanning indices of x
             if isinstance(L[i][j], (str, list, dict, tuple)) == True:             # checks if any of the elements                
                 return False, 'nonvalid data object type'                                          # cannot use it as a matrix
    return True, 'valid'

def vecnum_test(x):
    # function: input any object
    # output: binary True correspond to a 'list of numbers', ie, vector
    # False correspond to theb elements of x are and object different than a scalar
    if isinstance(x, list) == True:
        # if the object x is a list, then
        L = len(x[:])
        # store length of x in L
        for i in range(L):
            # ranging over all indices of x
            if isinstance(x[i], (int, float, complex)) != True:
                # if x[i], the ith element of x is not an integer, float, or complex, then
                return False
                # x is NOT a vector of numbers
        return True

# input:fundamental object
# output: if the list can be realized as a matrix (string)
def vector_matrix_test(A):
    n = len(A)
    if n == 0:
        return False, "empty list"
    elif n == 1 and isinstance(A[0], (int, float, complex)) == True:
        return True
    elif n >= 2:
        x = [0 for i in range(n)]
        for i in range(n):
            if isinstance(A[i], (int, float, complex)) == True:
                return True,'row vector'
            elif isinstance(A[i], (list, tuple)) == True:
               x[i] = len(A[i])
               j = i
               if i >= 1 and x[i] != x[i - 1]:
                   return False, 'sublength variation occurs not matrix'
        if len(A[0]) == 1:
            return True, 'column vector'
        else:
            if detect_type(A)[0] == False:
                return False, 'not a matrix'
            else:
                return True, 'true matrix'
            
N = []
# print(vector_matrix_test(N))

M = [[1, 2, 3], [3, 4]]
# print(vector_matrix_test(M))

A = [[1, 0], [0, 1]]
# print(vector_matrix_test(A))

B = [1, 2, 3, 4]
# print(vector_matrix_test(B))

C = [[1], [2], [3]]
# print(vector_matrix_test(C))

D = [[[1, 0],0], [0, 1]]
# print(vector_matrix_test(D), 'D')
