
def partition(arr, low, high):

    pivot = arr[high]
    mid = low  # mid is also the traverser

    while mid <= high:

        if arr[mid] < pivot:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        
        elif arr[mid] == pivot:
            mid += 1
        
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    
    # arr between p1 p2 is sorted so we need to 
    # sort left of p1 and right of p2
    p1 = low - 1
    p2 = high + 1

    return p1, p2 



def modified_quicksort(arr, low, high):

    if low >= high:
        return 
    
   
    p1, p2 = partition(arr, low, high)
    modified_quicksort(arr,low, p1)
    modified_quicksort(arr, p2, high)


def qsort_using_dutch_flag(arr):

    low, high = 0, len(arr)-1
    modified_quicksort(arr, low, high)
    return arr



tc = int(input())
for _ in range(tc):

    n = input()
    arr = [int(x) for x in input().split()]
    qsort_using_dutch_flag(arr)
    print(arr)