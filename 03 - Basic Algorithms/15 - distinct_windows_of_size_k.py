'''
We use hashmap + sliding window

hashmap to keep count of freq
sliding window of size k which slides iterates over all elements.

We first genrate hashmap of first k elements
then we go on removing one ele from start of window and add new element at end to calculte the distinct
element count which is nothing but the length of hashmap
'''

from collections import defaultdict

def countDistinctElements(arr, k):
    
    n = len(arr)
    ans = list()
    hashmap = defaultdict(int)

    # add first k elements
    for i in range(k):
        hashmap[arr[i]] += 1

    ans.append(len(hashmap))

    # Iterate through remaining elements
    for i in range(k,n):

        # decrement first element freq present in window if zero remove it
        # first element is k places behind
        element = arr[i-k]
        hashmap[element] -= 1

        if hashmap.get(element, None) == 0:
            hashmap.pop(element)
        
        # add new element to hashmap
        hashmap[arr[i]] += 1

        ans.append(len(hashmap))

    return ans

for _ in range(int(input())):

    n,k = map(int, input().split())
    arr = [int(x) for x in input().split()]
    print(*countDistinctElements(arr,k))