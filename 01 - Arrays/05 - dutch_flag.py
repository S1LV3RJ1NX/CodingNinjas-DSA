from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def sort012(arr, n) :

    low,mid = 0, 0
    high = n-1

    while mid <= high:

        if arr[mid] == 0:
            # Swap mid and lo
            arr[low],arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            # no swap
            mid += 1
        elif arr[mid] == 2:
            # swap mid and high
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    
    return arr



#taking inpit using fast I/O
def takeInput() :
    n = int(input().strip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n



def printAnswer(arr, n) :
    
    for i in range(n) :
        
        print(arr[i],end=" ")
        
    print()
    
#main

t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    sort012(arr, n)
    printAnswer(arr, n)
