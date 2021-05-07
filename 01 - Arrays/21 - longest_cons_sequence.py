# https://www.youtube.com/watch?v=qgizvmgeyUM&ab_channel=takeUforward 
# https://www.geeksforgeeks.org/longest-consecutive-subsequence/ 

from sys import stdin

def lengthOfLongestConsecutiveSequence(arr,n):

    unique_nos = set(arr)
    longest_seq = 0

    for ele in unique_nos:

        #  curr element is starting of sequence
        if ele-1 not in unique_nos:
            curr = ele 
            while curr in unique_nos:
                curr += 1

            longest_seq = max(longest_seq, curr-ele)
    
    return longest_seq

t = int(stdin.readline().rstrip())

while t > 0:
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(lengthOfLongestConsecutiveSequence(arr,n))
    t-=1
