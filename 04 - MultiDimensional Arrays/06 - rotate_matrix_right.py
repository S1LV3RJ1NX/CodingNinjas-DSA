import sys
from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def rotateMatRight(mat, n, m, k):
	# Create a temp array and rotate row wise.

    '''
    N = row, M = col
    This approach is based on the fact that when we rotate an array to the right by ‘K’ times, 
    it shifts ‘K’ elements from the end to the beginning of the array while the remaining elements shift 
    towards the end. The effective rotations in ‘MAT’ can be from 0 to 'M' - 1, as we get the same matrix 
    ‘MAT’ after every 'M' rotations. So, we will set ‘K’ to ‘K’ % ‘M’.
    '''
    ans = []

    k = k%m 

    for i in range(n):
        mat[i] = mat[i][(m-k):]+mat[i][:(m-k)]
        ans += mat[i]

    return ans

# Taking the input.
def takeInput() :
	n, m, k = map(int, sys.stdin.readline().strip().split(" "))
	mat = [list(map(int, sys.stdin.readline().strip().split(" "))) for row in range(n)]
	return n, m, k, mat

# Printing the Matrix.
def printAns(ans):
	for i in ans:
		print(i, end = ' ')
	print('')

# Main.
t = int(input().strip())
for i in range(t):
	n, m, k, mat = takeInput()
	ans = rotateMatRight(mat, n, m, k)
	printAns(ans)