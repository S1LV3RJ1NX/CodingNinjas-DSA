'''
The basic idea is to create an array for all rows and an array for all columns 
in which we will keep the information of those rows and columns whose value we 
need to set as 0 for the entire row and column.
 
We will create array rows of size N and array columns of size M. The array rows will 
keep the record of all rows, and the array columns will keep the record for all columns 
whose value of all elements we need to set to 0. Initially, all elements of rows and columns 
will contain the value 0. We will set the element’s value to 1 if we need to set all element 
values present in that particular row or column to 0.

Time Complexity: O(N * M)
Space Complexity: O(N + M)
'''

def findGoodMatrix(arr):

    n = len(arr)
    m = len(arr[0])

    rows = [0 for i in range(n)]
    cols = [0 for i in range(m)]

    # traverse th' array
    for idx in range(n):
        for pos in range(m):

            if arr[idx][arr] == 0:
                rows[idx] = 1
                cols[pos] = 1

    for idx in range(n):
        for pos in range(m):
            if rows[idx] == 1 or cols[pos]==1:
                arr[idx][pos] = 0

    return arr