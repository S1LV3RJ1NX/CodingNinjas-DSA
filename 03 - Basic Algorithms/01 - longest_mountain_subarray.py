"""
Logic is simple we need to find a mountain that is elements are first increasing
then decreasing. We can count all possible subarrays and check if it's a mountain.

Two pointer approach can also be used in a way:
When there is increasing subarray, mark the beginning index with the ‘START’ pointer.
Reset the value of both the ‘START’ and ‘END’ pointer, since it marks the beginning.
When there is a decreasing subarray, mark the ending index with the ‘END’ pointer.
Calculate the length of the current subarray ('END' - ‘START’ + 1) and take the maximum of all such lengths.
Finally return the maximum length that can be achieved.

There is another way in which we can use the 2 pointers approach. 
We know that every mountain has a peak so what we can do is assume every element to be peak and,
traverse a pointer to it's left until elements go on decreasing and decreasing. Similarly, traverse
elements to right untill ele are increasing and increasing. Once the trend breaks, we calculate the length
and store the maximum
"""

def is_peak(arr, idx):
    return (arr[idx] > arr[idx-1]) and (arr[idx] > arr[idx+1])

def longestMountain(arr, n):

    if n<3:
        return 0
    
    max_mountain_len = 0
    i=1

    while i<n-1:

        if is_peak(arr,i):
            # Initialize left and right pointers
            left, right = i,i

            # Traverse left
            while (left>0 and arr[left] > arr[left-1]):
                left -= 1
            
            # Traverse right
            while (right < n-1 and arr[right] > arr[right+1]):
                right += 1

            max_mountain_len = max(max_mountain_len, right-left+1)
            # reassign right for choosing next mountain as it will be next peak
            i = right 
        else:
            i+=1

    return max_mountain_len

tc = int(input())

for _ in range(tc):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(longestMountain(arr, n))
