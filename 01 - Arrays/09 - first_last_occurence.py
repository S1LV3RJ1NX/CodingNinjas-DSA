from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(10 ** 7)

def first_occurence(arr, target, low, high):

    mid = low + (high-low)//2
    # print(low, mid, high)
    if arr[mid] == target and (mid==0 or target > arr[mid-1]):
        return mid

    if low <= high:
        # Since we are finding first occurence check if target is greater or not
        if target > arr[mid]:
            return first_occurence(arr, target, mid+1, high)
        else:
            return first_occurence(arr, target, low, mid-1)
    return -1

def last_occurence(arr, target, low, high, N):

    mid = low + (high-low)//2

    if arr[mid] == target and (mid==N-1 or target < arr[mid+1]):
        return mid

    if low <= high:
        # Since we are finding last occurence check if target is less or not
        if target < arr[mid]:
            return last_occurence(arr, target, low, mid-1, N)
        else:
            return last_occurence(arr, target, mid+1, high, N)
    return -1


def findFirstLastPosition(arr, N, X):

    # Write your code here
    # Return a tuple containing two integers denoting the first and last occurrence of X
    first, last = -1, -1

    first = first_occurence(arr, X, 0, N-1)
    last = last_occurence(arr, X, 0, N-1, N)

    return first, last




# Taking input using fast I/0
def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    X = int(stdin.readline())
    return N, arr, X


tc = int(input())
while tc > 0:
    N, arr, X = takeInput()
    ans = findFirstLastPosition(arr, N, X)
    stdout.write(str(ans[0]) + " " + str(ans[1]) + "\n")
    tc -= 1
