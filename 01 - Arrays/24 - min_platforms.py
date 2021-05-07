# What we do is we keep track of arival and leaving times in sorted order
# if train arrives we increment the count, if leaves we decrement,
# We keep max until now to get our answer, similar to merge sort

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


def calculateMinPatforms(at, dt, n):

    at.sort()
    dt.sort()

    max_platforms = 1
    curr_platform = 1

    # imp initialization
    i,j = 1,0

    while i<n and j<n:
        if at[i] <= dt[j]:
            curr_platform += 1
            i += 1
        
        else:
            curr_platform -= 1
            j += 1
        
        max_platforms = max(max_platforms, curr_platform)

    return max_platforms


#   taking inpit using fast I/O
def takeInput():
    n = int(stdin.readline().strip())
    at = list(map(int, stdin.readline().strip().split(" ")))
    dt = list(map(int, stdin.readline().strip().split(" ")))

    return at, dt, n


#   main
T = int(input())
while (T > 0):
    T -= 1
    at, dt, n = takeInput()
    minNumOfPlatforms = calculateMinPatforms(at, dt, n)
    print(minNumOfPlatforms)
