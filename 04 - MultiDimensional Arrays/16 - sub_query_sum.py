'''
Auxiliary matrix
The basic idea is to create a matrix auxiliary with N rows and M columns 
in which auxiliary[r][c] will store the sum of the submatrix from (0 , 0) to (r , c). 
Using this idea, we can find the sum of the submatrix for each query in O(1) Space Complexity.

We can find the sum of the submatrix from (r1 , c1) to (r2 , c2) in the following way given below.
(Refer to image in the folder)

sum = auxiliary[r2][c2] - auxiliary[r2][c1 - 1] - auxiliary[r1 - 1][c2] + auxiliary[r1- 1][c1 - 1]

let matrix be
[
    1 1 1
    2 2 2
    3 3 3
]

initial aux arr will be
aux = 
[
    1 1 1
    0 0 0
    0 0 0
]

After col wise sum
aux = 
[
    1 1 1
    3 3 3
    6 6 6
]

After row wise sum
aux = 
[
    1  2  3
    3  6  9
    6 12 18
]
'''
def findSubmatrixSum(arr, queries):
    n = len(arr)
    m = len(arr[0])


    ans = []
    aux = [ [0 for j in range(m)] for i in range(n)]

    # Copy first row of arr into aux
    aux[0] = arr[0].copy()

    # update aux with colwise sum
    for idx in range(1,n):
        for pos in range(m):
            aux[idx][pos] = aux[idx-1][pos] + arr[idx][pos]

    # update aux with rowwise sum
    for idx in range(n):
        for pos in range(1,m):
            aux[idx][pos] += aux[idx][pos-1] 


    # traverse th' query
    for query in queries:
        # top left row, top left col
        # bottom right row, bottom right col
        top_lr, top_lc, bottom_rr, bottom_rc = query[:]

        sum_ = aux[bottom_rr][bottom_rc]

        # removing the upper section above the sq(refer img)
        if top_lr > 0:
            sum_ = sum_ - aux[top_lr - 1][bottom_rc]

        # removing the left section beside the sq(refer img)
        if top_lc > 0:
            sum_ = sum_ - aux[bottom_rr][top_lc - 1]

        # corner section subtracted twice hence add once 
        if top_lr > 0 and top_lc > 0:
            sum_ = sum_ + aux[top_lr - 1][top_lc - 1]

        ans.append(sum_)
    
    return ans

