'''
Suppose we have a task ('I', 'J'). Now we will update ith row and jth column of the matrix 
by 0. What can we conclude from this? We can say that the ith row and jth column will not contribute 
any empty cells. So we can just consider a matrix not having ith row and jth column. This means our 
number of rows has been reduced by one and the number of columns has also been reduced by 1.


Algorithm:

- Initialize 2 variables, rows by 'N' and columns by 'N'.
- Create an integer array of size 'K' namely outputArray.
- Take 2 sets, rowSet and colSet to keep track of the rows and columns we are eliminating.
- For every task ('I', 'J'), 
        - Check for 'I'
        - If 'I' is not present in rowSet, add it to the rowSet and reduce the number of rows by 1.
        - If 'I' is already present in the rowSet, we don’t have to do anything because this row has already been eliminated.
        - Check for 'J'
        - If 'J' is not present in colSet, add it to the colSet and reduce the number of columns by 1.
        - If 'J' is already present in the colSet, we don’t have to do anything because this column has already been eliminated.
        - Now the number of empty cells would be the product of the remaining rows and columns, insert it to the outputArray.
Return the outputArray.

'''
def emptyCells(N, K, tasks):
    # Write your code here.
    row, col = N,N
    row_set, col_set = set(), set()
    ans = []

    for i in range(K):
        r, c = tasks[i][0], tasks[i][1]

        if r not in row_set:
            row_set.add(r)
            row -=1
        
        if c not in col_set:
            col_set.add(c)
            col -= 1

        ans.append(row*col)
        
    return ans

test_cases = int(input())

while test_cases:

    N, K = map(int, input().split())
    tasks = []

    for t in range(K):
        i,j = map(int,input().split())
        X = i,j
        tasks.append(X)

    output = emptyCells(N, K, tasks)

    for emptyCell in output:
        print(emptyCell, end=' ')

    print()
    test_cases -= 1