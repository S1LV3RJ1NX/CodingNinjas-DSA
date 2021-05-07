def bestInsertPos(arr, n, target):

    low = 0
    high = n-1
    while low <= high:
        mid = low + (high-low)//2
        # If target present return
        if arr[mid] == target:
            return mid
        # Else if mid is less then go to right side.
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return high+1
    


tc = int(input())

for _ in range(tc):
    n, target = map(int, input().split())
    arr = [int(x) for x in input().split()]
    pos = bestInsertPos(arr, n, target)
    print(pos)




