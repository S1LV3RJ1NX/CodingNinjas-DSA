from sys import stdin, stdout, setrecursionlimit

# Ref: https://www.youtube.com/watch?v=f6YqGTpFKig
# The same algo gives AC on Leetcode but TLE here, hope they extend TimeLimit for python in future!
def findTriplets(arr, n):
    
    """
    Here we have to find all the triplets such that X+Y+Z=0. One approach will be to 
    generate all possible pairs and check for the sum but that will be most time consuming 
    Tc can range to O(n^3)

    Instead of finding 3 values that sum to zero we can find 2 values that equal to sum of
    negation of first basically: X+Y+Z=0 => Y+Z = -X, so for each given element in array
    we find two other elements whose sum equals to negation of the element. Thus we can use
    two pointer approach for each ele to find it's negation.

    Now another thing arisies is of handling duplicates. One method is to sort the array sorting
    brings duplicate elements together. So those can be easily skiped.Also sorting helps to increment
    and decrement pointers based on value of sum if it is greater or less than needed.

    So overall, we will have 3 pointers. One to traverse over all elements (basicaly upto n-3 ele)
    other 2 pointes will help us finding the negtaion sum.

    i -> 0 to n-3
    j (left pointer)  -> start from i+1 towards right 
    k (right pointer) -> start from n-1 toward left 
    """

    ans = []
    arr.sort()
    i=0

    # X = Y - Z
    while i < n-2:

        left, right = i+1, n-1
        value = -arr[i]

        # procedure similar to target pair sum
        # loop until the pointers don't cross each other
        while left < right:

            sum = arr[left]+arr[right]
            # sum less then req inc left
            if  sum < value:
                left += 1
            
            # sum more than required dec right
            elif sum > value:
                right -= 1
            
            # sum found
            else:
                ans.append([arr[i], arr[left], arr[right]])

                # skip similar left and right elements
                x = arr[left]
                y = arr[right]
                while left < right and arr[left] == x:
                    left += 1

                while left < right and arr[right]==y:
                    right -= 1

        # skip repeating elements
        while i+1<n-2 and arr[i] == arr[i+1]:
            i += 1
        
        i += 1

    return ans



# Taking input using fast I/0
def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return N, arr


tc = int(input())
while tc > 0:
    N, arr = takeInput()
    ans = findTriplets(arr, N)
    if len(ans) == 0:
        stdout.write("-1\n")
    else:
        for i in ans:
            i.sort()
            stdout.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")

    tc -= 1
