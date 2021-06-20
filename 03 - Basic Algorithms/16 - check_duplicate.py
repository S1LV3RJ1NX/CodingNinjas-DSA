'''
The problem is like for a window of size k if there are any duplicate elements,
within distance of k return True, else if no such ele exits for all possible windows,
return False

The idea is to process every window of size ‘K’ one at a time and store it into Set, 
now if the element is repeated in a window of size ‘K’ then we can say there is a duplicate within ‘K’ distance.

Initially, our window will contain the first ‘K’ element which is stored in Set.
Then for each remaining element, If it is already in the window return true. Otherwise, 
add it to the window. While adding the element in the window we have to also remove (i- ‘K’ - 1)th 
element from the current window i.e our Set.
'''

def checkDuplicate(arr, n, k):   
    
    window = set()

    for i in range(n):
        
        ele = arr[i]

        # duplicate found
        if ele in window:
            return True
        # else add to window
        else:
            window.add(ele)

        # For sliding window ,remove the (i-k)th from window.
        if i>=k:
            ele = arr[i-k]
            window.remove(ele)

    return False




for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = [int(x) for x in input().split()]
    print(checkDuplicate(arr, n, k))