'''
Approach: 
The simple idea is to remove a row or column in each comparison until an element is found. 

Start searching from the top-right corner of the matrix. There are three possible cases. 

The given number is greater than the current number: 
This will ensure that all the elements in the current row are smaller than the given number as 
the pointer is already at the right-most elements and the row is sorted. Thus, the entire row 
gets eliminated and continues the search for the next row. Here, elimination means that a row 
needs not be searched.

The given number is smaller than the current number: 
This will ensure that all the elements in the current column are greater than the given number. 
Thus, the entire column gets eliminated and continues the search for the previous column, i.e. 
the column on the immediate left.

The given number is equal to the current number: 
This will end the search.
'''
def search(matrix, x):
    # Write your code here.
    n = len(matrix)

    # right most ele
    i,j = 0, n-1

    while i<n and j >=0:

        if matrix[i][j] == x:
            return [i,j]

        # ele greater, reduce col
        elif matrix[i][j] > x:
            j -= 1
        
        # ele small, inc row
        else:
            i += 1

    return [-1,-1]



for _ in range(int(input())):
    N, X = map(int, input().split())
    mat = [[int(x) for x in input().split()] for i in range(N)]

    print(*search(mat,X))