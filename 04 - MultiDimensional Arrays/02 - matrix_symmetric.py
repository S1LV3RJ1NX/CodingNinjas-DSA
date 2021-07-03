def isMatrixSymmetric(matrix):
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True