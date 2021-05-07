def modified_bsearch(arr, low, high, target):
    
    # function returns the index of largest element
    # smaller than equal to 'x' in 'arr'. For duplicates
    # it returns the last index of occurrence of required
    # element. If no such element exits then it returns -1
    while low <= high:
        mid = low + (high-low)//2
        
        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
            
    return high+1



tc = int(input())
for _ in range(tc):
    n = int(input())
    arr_a = [int(x) for x in input().split()]
    k = int(input())
    arr_b = sorted([int(x) for x in input().split()])
    
    
    ans = []
    for ele in arr_a:
        ans.append(modified_bsearch(arr_b, 0, k-1, ele))
        
    print(*ans)
