'''
Traverse the matrix in form of spiral or cycles.
So a cycle can be divided into 4 parts, so if the cycle is of size m X n.
Element is in first row, i.e k <= m
Element is in last column, i.e k <= (m + n-1)
Element is in last row, i.e. k <= (m + n-1 + m-1)
Element is in first column, i.e k <= (m + n-1 + m-1 + n-2)
If any of the above conditions meet then the kth element can be found is constant time.
Else remove the cycle from the array and recursively call the function.
'''

def findK(matrix, n, m, k):

    if n<1 or m<1: 
        return -1

    # If ele is in the outermost ring

    # first row
    if k <= m:
        return matrix[0][k-1]
    
    # last col
    if k <= (m + n-1):
        return matrix[k-m][m-1]

    # last row
    if k <= ( m + n-1 + m-1):
        return matrix[n-1][m-1 - (k - (m + n-1))]

    # first col
    if k <= (m + n-1 + m-1 + n-2):
        return matrix[n-1 - (k - (m + n-1 + m-1))][0]


    # ele not in outermost ring
    matrix.pop(0)
    [j.pop(0) for j in matrix]
    return findK(matrix, n-2, m-2, k - (2*n + 2*m - 4))

def findKthElement(matrix, k):
    r,c = len(matrix), len(matrix[0])
    return findK(matrix, r, c, k)


for _ in range(int(input())):
    n , m, k = map(int, input().split())
    arr = [ [int(x) for x in input().split()] for i in range(n)]
    print(findKthElement(arr, k))