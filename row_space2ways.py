from transpose import transpose
from rank_col_space_basis import rank, col_space_basis
from row_i import row


### taking transpose of A, then computing columnspace
def row_space_t(A):
    tA = transpose(A)
    return col_space_basis(tA)

def row_space_std(A):
    rA = rank(A)
    r = rA[0]
    tildeA = rA[1]
    return [row(tildeA, i) for i in range(r)]
