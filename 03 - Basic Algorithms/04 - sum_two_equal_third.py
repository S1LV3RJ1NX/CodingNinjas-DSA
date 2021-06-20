from sys import stdin, stdout, setrecursionlimit

def findTriplet(arr, n):
    
    """
    Here we need to find a triplet where sum of 2 values will be equal to third.
    This problem can be thought of as extension of pair with target sum to zero,
    here instead of sum zero we check for the 3rd value in triplet.

    The question now arises which sum value to check? Since we need to find the triplet
    whose 2 values sum to third it's quiet intuitive to look for maximum value in the
    triplet. 

    So once we sort the arr instead of scanning elements from front, we scan them from
    back and for each element we initialize left and right pointers.

    let idx be index of choosen element then,
    left = 0, right = idx-1 

    and algorithm proceeds as usual depening upon current sum found based on if it is 
    more or less than the required value.
    """

    arr.sort()

    # X = Y + Z
    for i in range(n-1,-1,-1):

        left, right = 0, i-1

        # procedure similar to target pair sum
        # loop until the pointers don't cross each other
        while left < right:
            value = arr[i]

            # sum less then req inc left
            if arr[left]+arr[right] < value:
                left += 1
            
            # sum more than required dec right
            elif arr[left] + arr[right] > value:
                right -= 1
            
            # sum found
            else:
               return [arr[left],arr[right],value]
    return []



# Taking input using fast I/0
def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return N, arr


tc = int(input())
while tc > 0:
    N, arr = takeInput()
    if findTriplet(arr, N):
        print(True)
    else:
        print(False)
    

    tc -= 1
