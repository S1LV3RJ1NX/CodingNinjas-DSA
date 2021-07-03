# https://www.youtube.com/watch?v=63fPPOdIr2c

'''
A median is an element that has 1/2 ele before it and 1/2 ele after it.
Since the matrix is sorted row wise, one idea is to use binary search
to find the median.

We shall keep our search space as per the constraints here,
it will be 1 --> 10^5 now then we shall traverse each row 
and for every mid we shall count how many ele are <= mid

if the count is half of total no of ele in matrix we found our ans
'''
def count_less_than_equal_to_mid(arr, mid):

    low, high = 0, len(arr)-1

    while low <= high:
        md = (low + high) >> 1
        
        if arr[md] <= mid:
            low = md + 1
        else:
            high = md - 1

    return low

def getMedian(matrix):

    # Binary search on entire search space
    low, high = 1, 10**5
    row, col = len(matrix), len(matrix[0])

    while low <= high:
        mid = (low + high) >> 1
        # print(mid)
        count = 0

        # for each row count no of elements <= mid
        for i in range(row):
            count += count_less_than_equal_to_mid(matrix[i], mid)
        
        # print("CT: ",count)
        if count <= ( (row*col)//2):
            low = mid + 1
        else:
            high = mid - 1

    return low



for _ in range(int(input())):
    n ,m = map(int, input().split())
    matrix = [ [int(x) for x in input().split()] for i in range(n)]
    print(getMedian(matrix))