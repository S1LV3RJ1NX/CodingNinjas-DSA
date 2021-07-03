'''
The idea is to preprocess the given square matrix. In the preprocessing step, 
calculate sum of all vertical strips of size k x 1 in a temporary square matrix stripSum[][]. 
Once we have sum of all vertical strips, we can calculate sum of first sub-square in a row as 
sum of first k strips in that row, and for remaining sub-squares, we can calculate sum in O(1) 
time by removing the leftmost strip of previous subsquare and adding the rightmost strip of new 
square. 

Let n = 5, k = 3

arr = 
[ 
    1 1 1 1 1
    2 2 2 2 2
    3 3 3 3 3
    4 4 4 4 4
    5 5 5 5 5
]

After pre-processing, i.e, finding all vertical strips of size 3*3

[
    6  6  6  6  6
    9  9  9  9  9
    12 12 12 12 12
]

Now we add k eles in each row and go on adding next ele by removing new ele

[
    18 18 18
    27 27 27
    36 36 36
]
'''

def sumOfKxKMatrices(arr:list, k:int):
    # Write your code here.

    n = len(arr)
    if k > n:
        return -1

    # Preprocessing
    # strip will be of n cols but n-k+1 rows
    strip_sum = [ [0 for i in range(n)] for j in range(n-k+1)]

    # final ans will be n-k+1 * n-k+1 matrix
    ans = [[0 for i in range(n-k+1)] for j in range(n-k+1)]

    # Go col by col
    for j in range(n):

        sum_ = 0
        # Initial col upto k rows
        for i in range(k):
            sum_ += arr[i][j]
        
        # considering above exam this value for fst itern corresponds to 6
        # the ele in 0th row and 0th col
        strip_sum[0][j] = sum_ 

        # calculate sum of remaining rectangles
        # by going from 1st row to n-k+1th row
        # we remove the prev ele and add new ele
        for i in range(1, n-k+1):
            sum_ += (arr[i + k - 1][j] - 
                arr[i-1][j]) 
            strip_sum[i][j] = sum_  

    # At the end of this loop we shall get matrix of 6,9,12 as in above ex    

    # Calculate sum of sub-sq
    for i in range(n-k+1):
        sum_ = 0
        for j in range(k):
            sum_ += strip_sum[i][j]

        ans[i][0] = sum_
        # Calculate sum of remaining squares
        # in current row by removing the leftmost 
        # strip of previous sub-square and adding
        # a new strip
        for j in range(1, n-k+1):
            sum_ += (strip_sum[i][j+k-1] - strip_sum[i][j-1])
            ans[i][j] = sum_ 
        

    return ans


for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = [ [int(x) for x in input().split()] for i in range(n)]
    print(*sumOfKxKMatrices(arr, k))