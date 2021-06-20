'''
In this problem we are given some fruits but we have only 2 baskets,
we need to select the longest subarray such that that subarray has 
only 2 kinds of fruits.

This problem resembles to finding the subaray which has no more than
2 distinct characters. We can use sliding window for the same.

We shall add fruits to window until distinct chars <= 2
once it happens we shall cal the len and do window reduction,
simultaneously adding new elements.
'''

from collections import defaultdict

def findMaxFruits(string, n):

    maxlen = 0
    start, end = 0, 0
    hashmap = defaultdict(int)

    while end < n:
        fruit = string[end]

        hashmap[fruit] += 1

        # shrink window if distinct char > 2
        while len(hashmap) > 2:
            start_fruit = string[start]
            # Reduce freq of this fruit
            hashmap[start_fruit] -= 1

            # if freq is 0 remove it
            if hashmap.get(start_fruit) == 0:
                hashmap.pop(start_fruit)

            # inc start
            start += 1 

        maxlen = max(maxlen, end-start+1)
        end += 1

    return maxlen
    
        




for _ in range(int(input())):

    n = int(input())
    string = input().strip()
    print(findMaxFruits(string, n))
