'''
An array is called Switching if all the elements at even indices are equal and all the elements at odd indices are also equal.
So what we shall do is, initialize two vars EVEN and ODD with arr[0] and arr[1]

We shall then start traversing from arr[2]....arr[n-1]

If idx is even, we shall check if the ele matches with EVEN if so then continue
if it does not match we need to calculate max len so far, it will be max(maxlen, i-start)
now new start will be (i - 1) as we are atleast sure till prev ele.
update EVEN as arr[i] and ODD as arr[i-1]

similar for odd, just update EVEN as arr[i-1] and ODD as arr[i]

After the whole array got traversed then update 'MAX_LENGTH' to the maximum of 'MAX_LENGTH' and ‘N’ - ‘START’.
This is as the end sliding window len is not calculated during traversal
'''

def switchingSubarray(arr, n): 

    if n<=2:
        return n

    max_len = 0
    start = 0
    EVEN, ODD = arr[0], arr[1]

    for i in range(2,n):

        # If even idx and ele not equal to EVEN
        if not i&1 and arr[i] != EVEN:
            # print("Updating...",max_len, i, start)
            max_len = max(max_len, i-start)
            start = i-1
            EVEN = arr[i]
            ODD = arr[i-1]

        # Odd idx and ele not equal to ODD
        elif i&1 and arr[i] != ODD:
            # print("Updating...",max_len, i, start)
            max_len = max(max_len, i-start)
            start = i-1
            EVEN = arr[i-1]
            ODD = arr[i]

    # print(max_len, n, start)
    return max(max_len, n-start) 


for _ in range(int(input())):

    n = int(input())
    arr = [int(x) for x in input().split()]
    print(switchingSubarray(arr, n))