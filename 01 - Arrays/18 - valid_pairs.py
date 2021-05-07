# https://codezen.codingninjas.com/practice/470/2305/valid-pairs

from sys import stdin

def isValidPair(arr,n,k,m):

    # array of odd len cannot form pairs
    if n&1:
        return False

    from collections import defaultdict
    
    # create remainder map containing occurences of all remainders
    remainder_map = defaultdict(int)
    for ele in arr:
        rem = ele%k
        remainder_map[rem] += 1

    for rem, count in remainder_map.items():
        # check if curr rem divides m in 2 halves
        # if yes, then it must have even occurances to form pairs
        # else we can't form pairs
        if rem*2 == m and count&1:
            return False

        # else number of occurences of this remainder
        # must be equal to no of occurences of other part
        # of the remainder.
        # Subtraction can be negative hence we add +k and take %k
        if count != remainder_map[(m-rem+k)%k]:
            return False 

    return True
            
#Main
t=int(input())

while t>0:
    n = int(input())
    arr = [int(i) for i in input().split()]
    li = stdin.readline().rstrip().split(" ")
    k = int(li[0])
    m = int(li[1])
    print(isValidPair(arr,n,k,m))
    t -= 1


