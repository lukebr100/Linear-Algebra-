from row_i import row

def rowscale_0(A, i, c):
    if i < len(A) and c != 0:
        # Create a new matrix B with the same values as A
        Ri = row(A, i)
        for j in range(len(Ri)):
            Ri[j] = c * Ri[j]
        return Ri
    else:
        return 'invalid row or scalar'

def rowscale_1(A, i, c):
    if i < len(A) and c != 0:
        # Create a new matrix B with the same values as A
        B = [row[:] for row in A]
        Ri = B[i]
        for j in range(len(Ri)):
            Ri[j] = c * Ri[j]
        return Ri
    else:
        return 'invalid row or scalar'
A = [[1, 2], [3, 4]]  
# print(rowscale(A, 1, 2))


#input, matrix A rows i, j and nonzero c
#output, c * Ri + Rj \rightarrow Rj, the second Rj in this expressesion
def rowadd(A, i, j, c):
    B = A
    Ri = rowscale_0(B, i, c)
    Rj = row(B, j)
    n = len(Ri)
    for k in range(n):
        Rj[k] = Ri[k] + Rj[k]
    B[j] = Rj
    return B 

def rowswap(A, i, j):
    B = A
    Ri = row(B, i)
    Rj = row(B, j)
    
    t = Rj
    B[j] = B[i]
    B[i] = t
    return B


A = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
# print(rowscale_0(A, 0, -6))  # desired output w/ row_i.py row function

A = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
# print(rowscale_1(A, 0, -6))  # desired output

A = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]

# print(rowadd(A, 0, 1, -6))


A = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
# print(rowswap(A, 0, 1))
