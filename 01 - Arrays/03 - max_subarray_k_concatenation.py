#  The only problem here is we need to get to next array after 
# finishing the current one for that we can create an array of 
# size n*k and then apply Kadane's algorithm or a better way would be
# to use modulo arithmetic to reach to beginning of array

from sys import stdin
tc = int(input())

for _ in range(tc):
    n,k = map(int, input().split())
    arr = [int(x) for x in stdin.readline().strip().split(" ")]

    # sum can be negative
    max_sum, curr_sum = -float('inf'),0
    for i in range(n*k):
        curr_sum =curr_sum + arr[i%n]
        max_sum = max(max_sum, curr_sum)
        # reset curr_sum to 0 if negative
        curr_sum = max(curr_sum, 0)
    print(max_sum)

