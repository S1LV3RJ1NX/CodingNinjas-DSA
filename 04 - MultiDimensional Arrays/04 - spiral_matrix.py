import sys
from sys import stdin

'''
We will need 4 traversals
1) col_start to col_end ( inc row_start )
2) row_start to row_end (dec col_end )
3) col_end to col_start ( dec row_end )
4) row_end to row_start (int col_start )

Until row_start <= row_end and col_start <= col_end
'''
def spiralPathMatrix(matrix, n, m):
    # Write your code here.
    ans = []
    row_start, row_end = 0, n-1
    col_start, col_end = 0, m-1
    row_traverser, col_traverser = 0,0

    while row_start <= row_end and col_start <= col_end:

        # Left to Right
        col_traverser = col_start
        while col_traverser <= col_end:
            ans.append(matrix[row_start][col_traverser])
            col_traverser += 1
        row_start += 1

        # Top right to Bottom right
        row_traverser = row_start
        while row_traverser <= row_end:
            ans.append(matrix[row_traverser][col_end])
            row_traverser += 1
        col_end -= 1

        # Right to Left
        if row_start <= row_end:
            col_traverser = col_end
            while col_traverser >= col_start:
                ans.append(matrix[row_end][col_traverser])
                col_traverser -= 1
            row_end -= 1

        # Bottom left to top left
        if col_start <= col_end:
            row_traverser = row_end
            while row_traverser >= row_start:
                ans.append(matrix[row_traverser][col_start])
                row_traverser -= 1

            col_start += 1

    return ans




t = int(input().strip())

for j in range(t):
    
    n, m = list(map(int, stdin.readline().strip().split(" ")))
    
    arr = []
    
    for i in range(n):
        
        a = list(map(int, stdin.readline().strip().split(" ")))
        arr.append(a)
            
    
    for i in spiralPathMatrix(arr, n, m):
        print(i, end = " ")
        
    print()