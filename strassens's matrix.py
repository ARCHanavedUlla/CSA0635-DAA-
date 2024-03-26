def strassen_matrix_multiply(A, B):
    n = len(A)

    # Base case: If the matrices are 1x1, simply multiply
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # Splitting matrices into quarters
    mid = n // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Strassen's formula calculations
    S1 = [[B12[i][j] - B22[i][j] for j in range(mid)] for i in range(mid)]
    S2 = [[A11[i][j] + A12[i][j] for j in range(mid)] for i in range(mid)]
    S3 = [[A21[i][j] + A22[i][j] for j in range(mid)] for i in range(mid)]
    S4 = [[B21[i][j] - B11[i][j] for j in range(mid)] for i in range(mid)]
    S5 = [[A11[i][j] + A22[i][j] for j in range(mid)] for i in range(mid)]
    S6 = [[B11[i][j] + B22[i][j] for j in range(mid)] for i in range(mid)]
    S7 = [[A12[i][j] - A22[i][j] for j in range(mid)] for i in range(mid)]
    S8 = [[B21[i][j] + B22[i][j] for j in range(mid)] for i in range(mid)]
    S9 = [[A11[i][j] - A21[i][j] for j in range(mid)] for i in range(mid)]
    S10 = [[B11[i][j] + B12[i][j] for j in range(mid)] for i in range(mid)]

    # Recursive matrix multiplications
    P1 = strassen_matrix_multiply(A11, S1)
    P2 = strassen_matrix_multiply(S2, B22)
    P3 = strassen_matrix_multiply(S3, B11)
    P4 = strassen_matrix_multiply(A22, S4)
    P5 = strassen_matrix_multiply(S5, S6)
    P6 = strassen_matrix_multiply(S7, S8)
    P7 = strassen_matrix_multiply(S9, S10)

    # Calculating result submatrices
    C11 = [[P5[i][j] + P4[i][j] - P2[i][j] + P6[i][j] for j in range(mid)] for i in range(mid)]
    C12 = [[P1[i][j] + P2[i][j] for j in range(mid)] for i in range(mid)]
    C21 = [[P3[i][j] + P4[i][j] for j in range(mid)] for i in range(mid)]
    C22 = [[P5[i][j] + P1[i][j] - P3[i][j] - P7[i][j] for j in range(mid)] for i in range(mid)]

    # Combining result submatrices into the final result
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(mid):
        for j in range(mid):
            result[i][j] = C11[i][j]
            result[i][j + mid] = C12[i][j]
            result[i + mid][j] = C21[i][j]
            result[i + mid][j + mid] = C22[i][j]

    return result

# Example usage
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
B = [[17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]]
result = strassen_matrix_multiply(A, B)
for row in result:
    print(row)
