"""
Overall logic is like:
- We assume initial window to be entire array given by start, end
- We generate variable windows using 2 pointers i,j and store their freq count in map
- The condition to decrease window size is when distinct chars in map become equal to k, like aaab, ab, aaabbb have
2 distinct chars but we need to find the window which has min chars but they are distinct.
"""

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)
from collections import defaultdict

def smallestSubarrayWithKDistinct(arr, k) :

    hash_map = defaultdict(int)
    l = len(arr)

    # start, end will be initialized to start idx and end idx of array as it is possible that
    # smallest length will be entire array
    # end must be l-1 but we keep it as l so that it becomes easy to identify if window has changed or not
    start, end = 0,l

    # i,j will be our current window positions, these shall be varing
    i,j = 0,0

    # count will keep track of distinct chars in window, can be done using len dict too
    count = 0

    while j<l:

        # Add elements to hash map and increment the count if unique element
        if not hash_map.get(arr[j],None):
            count += 1
        hash_map[arr[j]] += 1
        

        # While count of distinct elements equal to k
        # i.e, size of hash_map is k, remove elements from the window
        # and if currlen < windowlen, update it
        while count == k :
            curr_len = j - i 
            if curr_len < end - start:
                start = i
                end = j 

            hash_map[arr[i]] -= 1
            if hash_map.get(arr[i]) == 0:
                hash_map.pop(arr[i])
                count -= 1
            i += 1

        j += 1

    if end==l:
        return [-1] 

    return [start, end]
        






#taking inpit using fast I/O
def takeInput() :

    n_k = stdin.readline().strip().split(" ")
    n = int(n_k[0].strip())
    k = int(n_k[1].strip())

    if n == 0 :
        return list(), 0, k

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n, k


#main
arr, n, k = takeInput()
print(*smallestSubarrayWithKDistinct(arr, k))
