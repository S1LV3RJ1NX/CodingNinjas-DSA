import sys

'''
Firstly, we can traverse the complete sequence of elements and calculate the total sum. We can store the total sum as ‘totalSum’. 
Create 2 variables ‘leftSum’ and ‘rightSum’. Initialize ‘leftSum’=0 and ‘rightSum’= ‘totalSum’. 

Then iterate through the sequence and do the following:


While traversing through the indices subtract the elements at the current index from 'rightSum’ .
If for any index, the ‘leftSum’ is equal to ‘rightsum’, we add that index as the equilibrium index in the answer sequence.
Add the element at the current index to ‘leftSum’ before checking for the next index.
 
Finally, return the answer sequence formed. 
'''

def findEquilibriumIndices(sequence):
    n = len(sequence)
    ans = []

    left_sum, right_sum = 0, sum(sequence)

    for i in range(n):
       
        # remove the ele from rightsum
        right_sum -= sequence[i]

        if left_sum == right_sum:
            ans.append(i)

        left_sum += sequence[i]
        
    return ans
    
# Taking input using fast I/O
def takeInput():
    n = int(input())
    sequence = list(map(int, input().strip().split(" ")))
    return sequence, n

# Main
t = int(input())
while t:
    sequence, n = takeInput()
    print(*findEquilibriumIndices(sequence))
    t = t-1