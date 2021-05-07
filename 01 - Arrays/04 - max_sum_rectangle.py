# Ref: https://www.youtube.com/watch?v=-FgseNO-6Gk&ab_channel=BackToBackSWE
# Ref: https://www.codingninjas.com/codestudio/problem-details/maximum-sum-rectangle_1082564

from sys import stdin

def kadanes_algorithm(arr):

    max_sum, curr_sum = -float('inf'), 0

    for ele in arr:
        curr_sum = max(curr_sum+ele, ele)
        max_sum = max(max_sum, curr_sum)
        curr_sum = max(curr_sum, 0)

    return max_sum 

def maxSumRectangle(arr, rows, cols):

    max_rec_sum = -float('inf')

    for left in range(cols):
        # Applying Kadane's on this row will give us the top and bottom
        row_sum_arr = [0]*rows 

        for right in range(left, cols):

            for i in range(rows):
                # Calculate sum between current left and right for each ro
                row_sum_arr[i] += arr[i][right]

            max_row_sum = kadanes_algorithm(row_sum_arr)

            max_rec_sum = max(max_rec_sum, max_row_sum)

    return max_rec_sum

tc = int(input())
for _ in range(tc):
    rows,cols = map(int, input().split())
    arr = [[int(x) for x in input().split(' ')] for i in range(rows)]
    # print(arr)
    ans = maxSumRectangle(arr, rows, cols)
    print(ans)