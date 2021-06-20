from sys import stdin, stdout, setrecursionlimit

"""
The question is similar to pair with target sum to zero.
To check if sum is zero of any triplet we modified the equation as follows:
x+y+z = 0 => y+z = -x

Now we need to check,
x+y+z = k => y+z = k-x

thus we need to find two values whose sum is k-x and together they will form a triplet.
Also, triplets like 2,5,5 or 5,2,5 or 5,5,2 are all same hence repeated elements must be skipped
"""

def findTriplets(arr, n, k):
    ans = []
    arr.sort()

    i = 0
    # X = Y - Z
    while i<n-2:

        left, right = i+1, n-1

        value = k-arr[i]
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
                x = arr[left]
                y = arr[right]
                ans.append([arr[i], x, y])

                # skip similar left and right elements
                while left < right and arr[left] == x:
                    left += 1

                while left < right and arr[right]==y:
                    right -= 1
        
        # skip repeating elements
        while i+1<n-2 and arr[i] == arr[i+1]:
            i += 1

        i += 1

    return ans













# Taking input using fast I/0.
def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    K = int(stdin.readline())
    return N, arr,K


tc = int(input())
while tc > 0:
    N, arr,K = takeInput()
    ans = findTriplets(arr, N,K)

    if len(ans) == 0:
        stdout.write("-1\n")

    else:
        for i in ans:
            # i.sort()
            stdout.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")

    tc -= 1
