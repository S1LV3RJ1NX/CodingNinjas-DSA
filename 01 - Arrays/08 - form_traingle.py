# Sort and check if sum of 2 is more than 3rd

from sys import stdin


def possibleToMakeTriangle(arr):
    arr.sort()
    n = len(arr)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if arr[i]+arr[j] > arr[k]:
                    return True 
                break
            break


    return False





# Main code

t = int(input().strip())

for i in range(t):
    n = list(map(int, stdin.readline().strip().split(" ")))

    if len(n) > 1:
        arr = n
    else:
        arr = list(map(int, stdin.readline().strip().split(" ")))

    if (possibleToMakeTriangle(arr)):
        print("YES")
    else:
        print("NO")
