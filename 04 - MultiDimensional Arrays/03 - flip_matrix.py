'''
Flip Conditions:
1. The flip operation is performed only for the 0s in the original matrix, and not for the new 
0s formed as a result of flipping 1s in the original matrix.

2. If a cell is already flipped, don’t flip it twice.


Brute Force:
The main idea is to count the number of 1s in the same row or column as any of the 0 in the 
given matrix. To do that, we iterate through the matrix with the variable ‘i’ for the row and 
‘j’ for the column, and if for any cell ‘MAT’[i][j] = 0, we iterate through the ‘i’th row and 
‘j’th column and count the number of 1s in them and mark them as -1 so that we do not revisit 
them. Finally, we return the ‘COUNT’.


Optimized:
The main idea is to ensure that a particular row or column is already checked,  we need not check it 
again. We can do this by maintaining a visited array for rows and columns and checking every time 
we encounter a ‘0’ that if its row or column is already visited then we need not check it again.

Keeping the above idea in mind, we can have the following approach: 

1. Make two arrays ‘VISITED_ROW’ and ‘VISITED_COL’ each of size ‘N’ to store if any particular 
row is already checked or not, where ‘N’ is the number of rows and number of columns.
2. Then we traverse the matrix and store the position of the zeroes in an array of pairs.
3. Then we traverse the array with the position of zeroes and for each element of the array, we 
check if columns and rows are visited or not.
4. If not visited, we traverse the particular row or column and check the number of 1s in the column 
or row and increment the count and replace the 1 with -1 so we do not count it again.
5. Finally return the COUNT
'''

def countFlip(mat):
    # Write your code here.
    n = len(mat)

    visited_row = [False for x in range(n)]
    visited_col = [False for x in range(n)]
    # zero_pos_arr = []
    count = 0

    for i in range(n):
        for j in range(n):
            if mat[i][j] == 0:
                
                # Instead of storing the position and traversing again,
                # we traverse in the same iteration
                
                # Check for row
                if visited_row[i] == False:
                    # since row is not visited mark the 1's
                    # in that row as -1 and inc the count
                    for k in range(n):
                        if mat[i][k] == 1:
                            count += 1
                            mat[i][k] = -1

                    visited_row[i] = True 

                # Check for col
                if visited_col[j] == False:
                    for k in range(n):
                        if mat[k][j] == 1:
                            count += 1
                            mat[k][j] = -1
                    visited_col[j] = True

    return count


for _ in range(int(input())):
    n = int(input())
    arr = [[int(x) for x in input().split()] for i in range(n)]
    print(countFlip(arr))
