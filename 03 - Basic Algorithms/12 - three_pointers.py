"""
We need to find the max absolute difference between 3 pairs of numbers,
even though we have been given 3 arrays at a time we shal be looking at 3 numbers
from the arrays. 
Since the numbers are sorted, the max diff will be between max and min value between the 3 numbers.
We have to find the minimum from all such differences. 

Since we need to get minimum difference, we increment the index which has minimum value as,
that will increase the possiblity of getting a difference which is less than the previous one.
"""

def threePointer(X:list, Y:list, Z:list):
    # Write your code here
    # Return an integer denoting the minimum value of max(abs(X[i] - Y[j]), abs(Y[j] - Z[k]), abs(Z[k] - X[i])).
    
    minimum, maximum, difference = 1e9, -1e9, 1e9

    # Three pointers for 3 arrays
    i,j,k = 0,0,0

    lx, ly, lz = len(X), len(Y), len(Z)

    while i<lx and j<ly and k<lz:
        minimum = min(X[i], Y[j], Z[k])
        maximum = max(X[i], Y[j], Z[k])
        difference = min(difference, maximum-minimum)

        if minimum == X[i]:
            i += 1
        elif minimum == Y[j]:
            j += 1
        else:
            k += 1

    return difference


for i in range(int(input())):

    l1 = input()
    arr1 = [int(x) for x in input().split()]
    l2 = input()
    arr2 = [int(x) for x in input().split()]
    l3 = input()
    arr3 = [int(x) for x in input().split()]

    print(threePointer(arr1, arr2, arr3))