# Ref: https://www.codingninjas.com/codestudio/problem-details/sum-of-infinite-array_873335
MOD = 1000000007
def sumInRanges(arr, n, queries, q):

    prefix_sum = [0]*n 
    prefix_sum[0] = arr[0]

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1]+arr[i]

    # print(prefix_sum[-1],prefix_sum[93], prefix_sum[89])
    ans = []
    for query in queries:
        # Queries are 1 based idx
        # array is 0 bases so -1
        left = query[0] - 1
        right = query[1] - 1

        if left == 0:

            full_traversal_count_right = right//n
            remaing_traversal_right = right%n

            sum_right = (prefix_sum[-1]*full_traversal_count_right) + prefix_sum[remaing_traversal_right]
            ans.append(sum_right%MOD)
        
        else:
            # to get sum between 2 ranges we take sum till right
            # subtract from sum till left-1
            left = left - 1
            # print("left, right", left, right)
            full_traversal_count_left = left//n 
            full_traversal_count_right = right//n

            remaing_traversal_left = left%n 
            remaing_traversal_right = right%n

            # print(full_traversal_count_left, remaing_traversal_left)
            # print(full_traversal_count_right, remaing_traversal_right)
            sum_left = (prefix_sum[-1]*full_traversal_count_left) + prefix_sum[remaing_traversal_left]
            sum_right = (prefix_sum[-1]*full_traversal_count_right) + prefix_sum[remaing_traversal_right]

            ans.append((sum_right-sum_left)%MOD)

    return ans







tc = int(input())

for _ in range(tc):
    n = int(input())
    arr = [int(x) for x in input().split()]
    q = int(input())
    queries = [[int(x) for x in input().split()] for i in range(q)]
    ans = sumInRanges(arr, n, queries, q)    
    print(*ans)
    
