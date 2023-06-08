# Linear-Algebra-
# algorithms in lin al
#
# If a list of numbers in Python is a vector, then a list of equal length sub-lists is a matrix! A set of matrices expressed in this way is a list of lists of sub-lists, ie, list cubed! Perhaps the term ‘tensor’ also applies to a set of matrices as if one arranged them in a cube for n n×n matrices or rectangular prism if one has k number of m×n matrices. random is the only package I have imported. I use random in my function set_rand_mtrx to generate a set of K random matrices m×n with random integer or rational number entries in a set range and step size.
#
# MATLAB is short for Matrix Labrotory. MATLAB interprets 
    A = [1, 2, 3, 4] == [1 2 3 4]
# as a row vector whose ith component, 1 <= i <= 4, can be accessed by
    A[i]
# For instance, 
    A[1] == 1
# is true. Now if 
    A = [1; 2; 3; 4]
# then A is a column vector with the same 
    A[1] == 1
# as above. So, spaces or commas in MATLAB separate a 'list' of numbers into a row, and semicolons separate a list of numbers into a column. Similarly, in Python, if 
    A = [1, 2, 3, 4]
# A is a list whose ith component, 0 <= i <= 3, can be accessed by
    A[i]
# For instance, 
    A[0] == 1
# is true. Also, 
    A[:] == [1, 2, 3, 4]
# Moreover in MATLAB, if 
    A = [1 2 3 4;
         5 6 7 8]
# then A is a 2-dimensional array or matrix in MATLAB. MATLAB uses the following system for indexing.
    A[1][1] == 1
    A[1][:] == [1 2 3]        # first row, columns 1 through 3
    A[:][1] == [1; 5]         # every row, first column
#
#
#
# Writing code to perform Gaussian Elimination 
# on lists compatible with a matrix, I realized that I must think aboutn lists differently than matrices in MATLAB despite the similarity in notation above.
# If, for example, list A is a list of lists given by:
    A = [[1, 2, 3, 4], 
          [5, 6, 7, 8]]
# then
    A[0][:] == A[:][0] == A[0]
# is true and gives the first row if A happens to be a matrix.
# My problem was when thinking about A, I wrongly assumed that
    A[:][0] == [1, 5]
# is true.
# I discovered that Python interprets 
    A[:][0]
# as taking all elements (two sublists) of A then accessing the first one.
