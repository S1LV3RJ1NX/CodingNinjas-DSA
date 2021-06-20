"""
Here we have to find a container which can hold most water that is container with max area.

Area of container is formed by choosing two lines out of them the line with minimum height
will form the height and distance between two lines will form the width. Thus, 
height*width = area.

One may think of choosing the two lines with most height but the thing is they might be 
adjacent to one another hence chances are area will be small even though the height is big.

So brute force solution can be two get all possible pairs and get the max area.
Can we optimize this?

One thing for sure we know is, in best case max area will be the size of entire container i.e,
the area between the first and the last line. So what we can do is keep two pointers one at the
start and other at the end. Each time area is calculated if it is more than max we update it.

Now the question arises if we have one area how to choose the next line, if you would observe
closely, it only makes sense to choose the next line in direction where we had found the smaller 
line as, there is chance we might find a bigger line next and get increase in area. 
"""

def maxArea(height):
    
    max_area, min_height  = -1e9, 1e9
    left = 0
    right = len(height) - 1

    while left < right:

        if height[left] < height[right]:
            min_height = height[left]
            max_area = max(max_area, min_height*(right-left))
            # next line to be chosen for area will be from left section
            left += 1
        else:
            min_height = height[right]
            max_area = max(max_area, min_height*(right-left))
            right -= 1

    return max_area



       


tc = int(input())

for _ in range(tc):
    n = input()
    arr = [int(x) for x in input().split()]
    print(maxArea(arr))