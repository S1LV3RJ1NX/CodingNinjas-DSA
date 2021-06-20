'''
We first make a freq hash of PTR
then through sliding window, we cancel out chars in freq map
if our window size is equal to ptr we go on removing from start and adding new elements
'''

from sys import stdin
import sys


from collections import defaultdict
def findAnagramsIndices(n, m, st, ptr):

    hashmap = defaultdict(int)
    count = m 

    # generate freq map
    for char in ptr:
        hashmap[char] += 1

    start, end = 0,0
    ans = []

    while end < n:

        # if current char in st part of ptr cancel it of from freq map and move to next
        curr_char = st[end]
        if curr_char in hashmap:
            hashmap[curr_char] -= 1
            # if freq yet is 0 or more than it we have chance to look for other characters
            if hashmap[curr_char] >= 0:
                count -= 1

        # all chars matched append start index
        if count == 0:
            ans.append(start)

        # size of current window is equal to len of ptr
        if end-start+1 == m:
            # remove the char at start and if it's part of hashmap, restore it's freq
            if st[start] in hashmap:
                # if freq of the char in hashmap was 0 or more it means this was part of anagram
                # hence restore the count, else if it would have been negative no need to restore
                # the count
                if hashmap[st[start]] >= 0:
                    count += 1
                hashmap[st[start]] += 1

            start += 1

        end += 1
    
    return ans
    


# Taking input using fast I/O.
def takeInput():

    nums = list(map(int, input().strip().split(" ")))
    st = input()
    ptr = input()

    return nums, st, ptr


# Main.
t = int(input())
while t:
    nums, st, ptr = takeInput()
    n, m = nums
    answer = findAnagramsIndices(n, m, st, ptr)
    for ans in answer:
        print(ans, end=" ")
    print()
    t = t-1
