'''
Approach:

The idea behind this approach is that we will find the row with the maximum number of 1’s in a single scan. 
This would be done by starting from the top right corner of the array ARR.

We will keep two variables row which stores the index of the row with the maximum number of ones and currentColumn 
stores the index of the column till which we have traversed.

Start from the top-right corner and if that current cell value is equal to 1 then move left in that row until we 
find a cell that contains a zero and update the values of row and currentColumn side by side. Also, keep in mind 
that the value of currentColumn should be greater than or equal to 0.

And if the current cell value is equal to 1 then move to the next row.

Consider the following example:
We have ARR =  {{0, 0, 1, 1}, {1, 1, 1, 1}}.
So our row = -1 and currentColumn = 3(0-based indexing).
We are initially in the 0th row at cell {0, 3} and there is a 1 so we move left in that row till we found a zero. 
So we find the 0 at cell {0, 1} and at this point our row = 0 and currentColumn = 1 and the total number of 1’s we found are = 2.
Since we find the 0 at cell {0, 1} so we move to the next row. Here at cell {1, 1}, there is a 1 so we move towards the 
left and the cell {1,0} also contains 1 but now we can’t move left further so came out of the loop. At this point, 
our row = 1 and currentColumn = -1. Return the variable row with the value 1 as this row contains the maximum number of 1’s i.e 4.
 

Algorithm: 

- Create a variable currentColum initialized to M-1.
- Create another variable row initialized to -1.
- Now traverse for every row from i = 0 to i = N, and for each row, perform the following steps:
- Till the value of currentColumn is greater than or equal to 0 and ARR[i][currentColumn] = 1 then perform following steps:
    - Decrement currentColumn by 1.
    - Update the row with i.
- Finally, return row as the answer.
Time Complexity
O(N+M), where N is the number of rows, and M is the number of columns.
'''
def maxOne(arr):
    # Write your code here.
    n = len(arr)
    m = len(arr[0])

    current_col = m-1
    max_row = -1

    for i in range(n):
        while current_col >= 0 and arr[i][current_col] == 1:
            current_col -= 1
            max_row = i

    return max_row


for _ in range(int(input())):

    r , c = map(int, input().split())
    arr = [ [int(x) for x in input().split()] for i in range(r)]
    print(maxOne(arr))