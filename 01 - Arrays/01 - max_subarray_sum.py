from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :
    # Sum for empty subarray is 0
    if not arr:
        return 0
    
    max_sum, curr_sum = 0, 0
    
    for ele in arr:
        
        # We can add the current element to curr sum if it is +ve
        # else we can start new sum from that position
        curr_sum = max(curr_sum+ele, ele)
        
        # Finally we find maximum over all such sums
        max_sum = max(max_sum, curr_sum)

    return max_sum


#taking inpit using fast I/O
def takeInput() :
    
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
