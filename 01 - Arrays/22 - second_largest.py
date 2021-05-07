from sys import stdin
import sys


def findSecondLargest(sequenceOfNumbers):
    # Write your code here.
    
    unique_nos = set(sequenceOfNumbers)

    if len(unique_nos) < 2:
        return -1 

    max_no, second_max = -1e9, -1e9

    for ele in unique_nos:
        if ele > max_no:
            second_max = max_no 
            max_no = ele 

        # if element is between max and second max
        elif ele > second_max and ele != max_no:
            second_max = ele 

        # print(max_no, second_max)
    if second_max == -1e9:
        return -1 
    return second_max














# Taking input using fast I/O
def takeInput():
    n = int(input())

    sequenceOfNumbers = list(map(int, input().strip().split(" ")))

    return sequenceOfNumbers, n


# Main
t = int(input())
while t:
    sequenceOfNumbers, n = takeInput()
    print(findSecondLargest(sequenceOfNumbers))
    t = t-1
