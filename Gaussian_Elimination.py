# input:fundamental object
# output: if the list can be realized as a matrix (string)
def vector_matrix_test(A):
    n = len(A)
    if n == 0:
        return "empty list"
    elif n == 1 and isinstance(A[0], (int, float, complex)) == 1:
        return True
    elif n >= 2:
        x = [0 for i in range(n)]
        for i in range(n):
            if isinstance(A[i], (int, float, complex)) == 1:
                return 'row vector'
            elif isinstance(A[i], (list, tuple)) == 1:
               x[i] = len(A[i])
               j = i
               if i >= 1 and x[i] != x[i - 1]:
                   return 'sublength variation occurs not matrix'
        if len(A[0]) == 1:
            return 'column vector'
        else:
            return 'matrix'
            
N = []
print(vector_matrix_test(N))

M = [[1, 2, 3], [3, 4]]
print(vector_matrix_test(M))

A = [[1, 0], [0, 1]]
print(vector_matrix_test(A))

B = [1, 2, 3, 4]
print(vector_matrix_test(B))

C = [[1], [2], [3]]
print(vector_matrix_test(C))



# function, input: A matrix column to access
# output: ith column of A
def column(A, i):
    if vector_matrix(A) == 'row vector':                                        # input matrix is row vector
        return [[A[i - 1]]]
    elif vector_matrix(A) == 'column vector':                                   # input is column vector
         return [[sublist[0]] for sublist in A]
    elif vector_matrix_test(A) == 'matrix':                                   # input is matrix               
        i = i - 1
        return [[sublist[i]] for sublist in A]                                # output the ith entry of each sublist
    
    
print(column(A, 1))                 # 1st element of each sublist 

# input: matrix A, row to be accessed
# output: row i
def row(A, i):
    i = i - 1
    if vector_matrix_test(A) == 'row vector' and i == 1:
        return A
    elif vector_matrix_test(A) == 'matrix' or vector_matrix_test(A) == 'column vector':
        i = i - 1
        return A[i]
     else: 
        return A, 'is not a matrix'

print(row(A, 1))                    # first sublist of A






def detect_type(L):
    for i in range(len(L)):                                                     # every sublist of L                                            
        for j in range(L[i]):                                                   # for j spanning indices of x
             if isinstance(L[i][j], (str, list, dict, tuple)) == 1:             # checks if any of the elements                
                 return 'nonvalid data object type'                                          # cannot use it as a matrix
     return True
     




#input, matrix A rows i, j and nonzero c
#output, c * Ri + Rj \rightarrow Rj, the second Rj in this expressesion
def rowadd(A, i, j, c):
    Ri = row(A, i)
    Rj = row(A, j)
    n = len(Ri)
    for i in range(n):
        Rj[i] = c * Ri[i] + Rj[i]
    A[j] = Rj
    return A
    

Y = [[1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]]
    
# print( rowadd(Y, 0, 1, -4 ), 'rowadd' )

def rowswap(A, i, j):
    Ri = row(A, i)
    Rj = row(A, j)
    
    t = Rj
    A[j - 1] = A[i - 1]
    A[i - 1] = t
    return A



# detects if a matrix has a row of zeros and if it is the zero matrix
# input: A, matrix 
# output: number of zero rows
def detect_zeros(A):
    m = len(A)
    n = len(A[0])
    count = [0 for _ in range(n)]
    count_zeros = [0 for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if A[i][j] == 0:
                count[j] = 1
            else:
                break
        if sum(count) == n:
            count_zeros[i] = 1
    if sum( count_zeros ) == m:
        return 'zero matrix'
    elif 1 in count_zeros:
        return 'non-zero matrix with', sum(count_zeros), 'zero rows'
    else: 
        return 'nonzero matrix'

E1 = [[1, 2, 3], [1, 1, 1], [0, 0, 0]]   

print(detect_zeros(E1))

A = [[1, 2, 3],                        
    [4, 5, 6], 
    [7, 8, 9]]
print(detect_zeros(A))





def gaussian_elim(A): # gets scale factors for ith column
    if  matrix(A) == True and detect_type(A) == True:
        m = len(A)      # store number of sublists in A (rows)
                        #if matrix(A) == True and detect_list(A) == False and len(b) == m:       # checks if list is matrix compatible, there are no order higher than 2 of list of lists and the length of b is length of A
        n = len(A[0])       # store the number of columns of A
        C = [ [0 for _ in range(n)] for _ in range(m) ]      # initailizes a list of lists of all zeros 
        for i in range(n):              # arbitrary column       
            
            k = 0                       # counter
            for j in range(i, m - 1):   # row from i, i + 1, ..., m - 2
                if A[j - k][i] != 0:    # the pivot position is non-zero // j - k is constant in this loop   
                    t = A[j - k][i]     # store pivot
                    C[j + 1][i] = - (A[j + 1][i] / t)               # calculate factor
                    A = rowadd( A, j - k, j + 1, C[j + 1][i])       # perform row op
                    k = k + 1                                       # add to counter
        return A
    else:
        return "please input a matrix"
    

    


A = [[1, 2, 3],                               #works, result in REF
    [4, 5, 6], 
    [7, 8, 9]]
print(gaussian_elim( A ))

B = [[1, 2, 3, 4],                           # works
    [5, 6, 7, 8],
    [9, 10, 11, 12]]
print(gaussian_elim( B ), "B")

C = [[1, 2, 3], [4, 5, 6], [7,8, 9], [10, 11, 12]]      # works
print(gaussian_elim( C ))

D = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]           # works
print(gaussian_elim( D ), "D")

E = [[0, 0, 0], [1, 1, 1], [1, 2, 3]]           # matrix NOT in REF
print(gaussian_elim( E ))                       
E1 = [[1, 2, 3], [1, 1, 1], [0, 0, 0]]          # works
print(gaussian_elim( E1 ), "E1")
