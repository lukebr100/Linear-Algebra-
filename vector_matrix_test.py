from detect_type import detect_type

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