# https://www.youtube.com/watch?v=xFJXtB5vSmM&ab_channel=AdityaVerma

'''
The idea is to form a sliding window of size k and keep on getting the maximum elements.

The thing which will cause problem is when we add a new element in the window, and remove
the previous element and assume that element is max element, then how can we be sure that 
new element added will be maximum? We need a mechanism such that when we remove an ele from
the window, before adding the new element , maximum from the remaining portion of window
must be available to us so that it can be comapred with the new element to update the maximum.

We can have a deque for the same, where we shall be storing maximum elements.
The logic will be like, if you are adding an element into deque then pop from front 
all the elements which are less than the current as they won't be the canditates
basically remove elements which are to left of curr and less than current

e.g:
3 5 -2 -1 4

window size = k = 3

deque will have : 3
then when 5 arrives 3 is no longer needed as 5 > 3 hence deque: 5
then -2 arrives, -2 < 5, thus when 5 is removed in some process then remaining window size of 2 will be (-2,-1)
so -2 can be a candidate. When -1 arrives it is less than 5 hence won't be added to queue. and max will be 5

next when we add 4 deque is : -2 it more hence pop and max is 4

ALGO:
- Create a deque to store k elements.
- Run a loop and insert first k elements in the deque. Before inserting the element, 
check if the element at the back of the queue is smaller than the current element , if it is so 
remove the element from the back of the deque, until all elements left in the deque are greater than 
the current element. Then insert the current element, at the back of the deque.
- Now, run a loop from k to end of the array.
- Print the front element of the deque.
- Remove the element from the front of the queue if they are out of the current window.
- Insert the next element in the deque. Before inserting the element, check if the element 
at the back of the queue is smaller than the current element , if it is so remove the element 
from the back of the deque, until all elements left in the deque are greater than the current element. 
-Then insert the current element, at the back of the deque.
- Print the maximum element of the last window.
'''

# Dry run with ex: [7,5,-2,-1,4,2] and k=3

from collections import deque
def maximumInAllSubarraysOfSizeK(arr, n, k):
    
    if k == 1:
        return arr

    if k > n:
        return [max(arr)]

    dq  = deque()
    ans = []

    # procress first k elements
    for i in range(k):

        # while adding new elements check if all ele to left are less
        # if so pop them
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()

        dq.append(i)

    # procress rest of the elements
    for i in range(k,n):

        # ele at front of queue is largest of prev window
        ans.append(arr[dq[0]])

        # remove the ele which are out of the window
        while dq and dq[0] <= i-k:
            dq.popleft()

        # while adding new ele remove all ele which are less than curr
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()

        dq.append(i)

    # add max element of last window
    ans.append(arr[dq[0]])

    return ans


for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = [int(x) for x in input().split()]
    print(*maximumInAllSubarraysOfSizeK(arr,n,k))
