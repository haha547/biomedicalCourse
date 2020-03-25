import random
def zero_matrix(rows,cols):
    """
        rows : number of the matrix's rows
        cols : number of the matrix's columns

        return the rows*cols matrix
    """
    m =[]
    while len(m) < rows:
        m.append([])
        while len(m[-1]) < cols:
            m[-1].append(0.0)
    
    return m

def identity_matrix(n):
    """
        first thing first copy a square zero_matrix
        when matrix[i][i] = 1
    """
    IdM = zero_matrix(n, n)
    for i in range(n):
        IdM[i][i] = 1.0

    return IdM

def print_matrix(A):
    rows = len(A)
    cols = len(A[0])
    for i in range(rows):
        for j in range(cols):
            print("%.4f " %A[i][j],end="")
        print("\n")

def random_matrix(rows,cols):
    RM = zero_matrix(rows,cols)
    for i in range(rows):
        for j in range(cols):
            RM[i][j] = random.random()
    return RM

def copy_matrix(m):
    """
        new a zero matrix and write on the new one 
    """
    rows = len(m)
    cols = len(m[0])
    cm = zero_matrix(rows,cols)
    for i in range(rows):
        for j in range(cols):
            cm[i][j] = m[i][j]
    
    return cm

def transpose(m):
    rows = len(m)
    cols = len(m[0])
    MT = zero_matrix(cols, rows)
    for i in range(rows):
        for j in range(cols):
            MT[j][i] = m[i][j]
    
    return MT

def matrix_addation(A, B):
    """
        input two matrixs A and B and do the addation
    """
    # step one check two matrix are the same size
    row_A = len(A)
    row_B = len(B)
    col_A = len(A[0])
    col_B = len(B[0])
    if row_A != row_B or col_A != col_B:
        raise ArithmeticError('Matrices are NOT the same size.')
    # step two creat a new matrix to add on
    C = zero_matrix(rows=row_B,cols= col_B)
    for i in range(row_B):
        for j in range(col_B):
            C[i][j] = A[i][j] + B[i][j]
    
    return C

def matrix_subtraction(A, B):
    """
        input two matrixs A and B and do the subtraction
    """
    # step one check two matrix are the same size
    row_A = len(A)
    row_B = len(B)
    col_A = len(A[0])
    col_B = len(B[0])
    if row_A != row_B or col_A != col_B:
        raise ArithmeticError('Matrices are NOT the same size.')
    # step two creat a new matrix to add on
    C = zero_matrix(rows=row_B,cols= col_B)
    for i in range(row_B):
        for j in range(col_B):
            C[i][j] = A[i][j] - B[i][j]
    
    return C

def matrix_multiply(A,B):
    row_A = len(A)
    row_B = len(B)
    col_A = len(A[0])
    col_B = len(B[0])
    if col_A != row_B:
        raise ArithmeticError('Matrices can NOT do multiply.')
    C = zero_matrix(row_A, col_B)
    for i in range(row_A):
        for j in range(col_B):
            sum = 0
            for ii in range(col_A):
                sum += A[i][ii]*B[ii][i]
            C[i][j] = sum
    return C
    
def linear_Regression():
    return True

def matrix_sum(A):
    sum = 0
    rows = len(A)
    cols = len(A[0])
    for i in range(rows):
        for j in range(cols):
            sum += A[i][j]
    return sum

def matrix_mean(A):
    rows = len(A)
    cols = len(A[0])
    return matrix_sum(A)/(rows*cols)




