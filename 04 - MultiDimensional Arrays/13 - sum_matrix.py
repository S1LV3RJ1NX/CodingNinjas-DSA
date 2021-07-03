'''
Let's take the matrix

2 3 4

3 4 5 

4 5 6

 

Now we can see till 4 all the numbers are occurring number-1 times. And if we take 4 as the longest diagonal 
the number on both sides at an equal distance have the same number of time occurrence. So after the biggest diagonal,
the occurrence is  2*n+1-q. 

If ‘q’ is less than equal to ‘n+1’. Then we return ‘q-1’ as the answer.
In all other cases, we will return ‘2*n-q+1’ as the answer.
'''

def query(n, q):
    if q == 0 or q > 2*n:
        return 0
    if q <= n+1:
        return q-1
    else:
        # Mathematical computation
        return n + n + 1 - q