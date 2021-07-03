'''
For any 0 we just need to check its four adjacent sides and look for 1s in them. 
Therefore we could simply traverse the matrix, and if the current element is a 0, 
check how many of its adjacent neighbors are 1s and add this value to an integer 
variable ANS representing the result. In the end, return the value of ANS.
'''

def coverageOfMatrix(mat):

    n = len(mat)
    m = len(mat[0])

    ans = 0

    for i in range(n):
        for j in range(m):

            # if matrix is all 1 then to we count coverage
            # top
            if i-1 >= 0:
                ans += mat[i-1][j]
            # right
            if j+1 < m:
                ans += mat[i][j+1]

            # bottom
            if i+1 < n:
                ans += mat[i+1][j]
            
            # left
            if j-1 >= 0:
                ans += mat[i][j-1]

    return ans