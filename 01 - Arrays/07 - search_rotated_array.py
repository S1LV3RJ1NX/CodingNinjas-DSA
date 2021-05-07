from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def rotated_bsearch(arr, target, low, high):

    mid = low + (high-low)//2
    # print("Mid.",mid,arr[mid])

    if arr[mid] == target:
        return mid 

    if low <= high:
        # if LHS is sorted
        if arr[low] <= arr[mid]:
            # print("0.", low, high)
            if target < arr[mid] and target >= arr[low]:
                # print("1.",low, mid-1)
                return rotated_bsearch(arr, target, low, mid-1)
            else:
                # print("2.",mid+1, high)
                return rotated_bsearch(arr, target, mid+1, high)
        else:
            if target > arr[mid] and target <= arr[high]:
                # print("3.",mid+1, high)
                return rotated_bsearch(arr, target, mid+1, high)
            else:
                # print("4.",low, mid-1)
                return rotated_bsearch(arr, target, low, mid-1)

    return -1

def search(arr, target) :

    low, high = 0, len(arr)-1

    return rotated_bsearch(arr, target, low, high)







#taking inpit using fast I/O
def takeInput() :
    
    n = int(input())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
test =  int(input())
for i in range(test) :
    
    target = int(input())
    print(search(arr, target))
