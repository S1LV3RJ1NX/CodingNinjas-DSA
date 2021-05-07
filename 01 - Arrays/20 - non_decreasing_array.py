from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


def isPossible(arr, n):

    modified = 0
    for i in range(1,n):
        # inversion found
        if arr[i] < arr[i-1]:
            modified += 1
            if modified > 1:
                return False 
            
            # mountain pattern
            if i < 2 or arr[i-2] <= arr[i]:
                # lower arr[i-1]
                arr[i-1] = arr[i]
            else:
                # go ahead and slide down pattern
                # raise arr[i]
                arr[i] = arr[i-1]

    return True






def takeInput():

    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#   Main
T = int(input().strip())
while T>0:
    T-=1
    arr, n = takeInput()
    ans = isPossible(arr, n)
    if (ans):
        print("true")
    else:
        print("false")