from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

tc = int(input())

for _ in range(tc):
    n = input()
    arr = [int(x) for x in stdin.readline().strip().split(" ")]

    # What we need to do here is find that subarray which has 
    # more number of zeros and less number of ones, in other words
    # sub array such that difference between count of 0's and count
    # of 1's is large.

    # Here we are identifying the largest difference in subarray section
    # which is similar to finding largest sum (Kadane's algo !!). But how
    # to find the diff? what if we convert 0's to 1 and 1 to -1 and find diff?
    # Once we find the diff we add it to count of 1's and get out answer

    count1 = 0
    max_diff, curr_diff = 0, 0

    for ele in arr:
        if ele == 1:
            count1 += 1

        curr_value = 1 if ele == 0 else -1 
        curr_diff = max(curr_diff+curr_value, curr_value)
        max_diff = max(max_diff, curr_diff)

    print(count1+max_diff)

