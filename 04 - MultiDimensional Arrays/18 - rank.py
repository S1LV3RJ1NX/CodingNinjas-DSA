'''
- The idea is based on converting the given input matrix ARR into row echelon form.

- Since we know that the rank of the matrix can not be greater than min(N, M). 
So we will check if N > M then we will transpose the input matrix ARR since 
we are using row echelon form so the matrix has to be transformed in such a way 
that in each row all the elements to the left of the diagonal element must be zero. 
And the count of non-zero diagonal elements in each row will be equal to our rank of the matrix.

- Otherwise, we will proceed with the next step without performing the transpose of the 
given matrix ARR.

- Now we will traverse over each row and perform the following operations:
    * If the diagonal element is non-zero then we will make all the elements in that column 
    as zero except the diagonal element by finding the appropriate multiplier.

    * If it is zero then two cases arise:
        case1: If there is a row below the current row with a non - zero entry in the same 
        column then we will swap both of these rows.
        
        case2: if we are unable to find a row with a non -zero entry in the current column 
        then we will swap this current column with the last column.

    * Now we will decrement the number of rows by one so that the row can be processed again.

- Now we will iterate through all the rows and count the diagonal element which is equal to our 
rank of the matrix
'''

'''
   Time Complexity: O((N^2)*M)
   Space Complexity: O(N*M)

   Where 'N' is the number of rows and 'M' is the number of columns
'''

# Function to find the transpose of the matrix
def transpose(arr, n, m):

    temp = [[0 for i in range(n)] for j in range(m)]
    
    for i in range(n):
        for j in range(m): 
            temp[j][i] = arr[i][j];

    arr = temp
    return arr

# Function for swapping the rows
def swapRow(arr, n1, n2, m):

    for i in range(m):
        temp = arr[n1][i]
        arr[n1][i] = arr[n2][i]
        arr[n2][i] = temp
    
    return arr

# Function for swapping the columns
def swapCol(arr, m1, m2, n):

    for i in range(n):
        temp = arr[i][m1]
        arr[i][m1] = arr[i][m2]
        arr[i][m2] = temp
    return arr

def findRankOfMatrix(arr):

    n = len(arr)
    m = len(arr[0])

    # If number of N is greater then M then do transpose of the matrix
    if (n > m):
        arr = transpose(arr, n, m)
        n, m = m, n
    
    # Now create a variable swapCol equal to M - 1 which will be used when we have to swap the columns
    swapPos = m - 1

    i = 0
    # Iterate through each row
    while(i<n):
        # If there is a non-zero diagonal element then we have to make all the elements in the current column to zero except the diagonal element
        if (arr[i][i] != 0):
            for j in range(n):

                    if (j != i and arr[j][i] != 0):
                        multiplier = arr[j][i] / arr[i][i]

                        for k in range(m):
                            arr[j][k] -= multiplier * arr[i][k]

            # Increase i by 1 so we can process next row
            i += 1

        # If the diagonal element is zero
        else:
            # Find if there exists a row with a non - zero enetry in same column
            # If so swap these tow rows and break the loop
            isSwapped = False
            for j in range(i+1,n):
                
                if (arr[j][i]):
                    arr = swapRow(arr, i, j, m)
                    isSwapped = True
                    break

            # Now check if isSwapped is equal to false then swap the current column i with the column represented by swapCol and decrement the value of swapCol by one
            if (isSwapped == False):

                if (swapPos > i):
                    arr = swapCol(arr, i, swapPos, n)
                    swapPos -= 1

                else:
                    break

            
        
    # Rank will be equal to non-zero diagonal element in each row
    rank = 0
    for i in range(n):
        if (arr[i][i]):
            rank += 1
        else:
            break

    return rank
