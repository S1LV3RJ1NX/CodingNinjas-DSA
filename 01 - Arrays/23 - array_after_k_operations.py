from sys import stdin, stdout
# https://www.geeksforgeeks.org/print-the-array-after-k-operations/

def printArrayAfterKOperations(arr, N, K):
    max_ele = max(arr)
    min_ele = min(arr)

    if K != 0:
        if K&1:
            return [max_ele-ele for ele in arr] 
        else:
            return [ele-min_ele for ele in arr] 
    return arr


# Taking input using fast I/0
def takeInput():
    N, K = list(map(int, stdin.readline().strip().split(" ")))
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return N, K, arr


tc = int(input())
while tc > 0:
    N, K, arr = takeInput()
    sol = printArrayAfterKOperations(arr, N, K)
    for i in sol:
        stdout.write(str(i) + " ")
    stdout.write("\n")
    tc -= 1
