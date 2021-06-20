"""
Greedy Approach

We will do the two-pointer approach, Initialize the first pointer to the start of str1 and 
the second pointer to the start of the str2.

Now increase the first pointer till the character pointed by the first pointer in str1 matches 
the character at the second pointer in str2. And the number of character which did not match should 
be placed at the end of str1. Therefore increase our answer by how many times we needed to 
increase the first pointer.

Now character pointed by both the pointer is the same so simply increase both pointers as they are same. 
And perform this while both the pointer do not exhaust the str1 and str2 respectively.

One thing to note is that all the characters which did not match would be placed at the end optimally so 
that the cost will be equal to the unmatched characters with the prefix of str2.

Time Complexity:
    O(N+M) where N is the size of the first string and M is the size of the second string.

We are traversing both the strings only once.Thus time complexity is O(N+M). 
"""
from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)
from collections import defaultdict

def minCostToGivenString(str1, str2) :

    freq_map = defaultdict(int)

    # check if chars in str1 match str2

    for char in str1:
        freq_map[char] += 1

    for char in str2:
        freq_map[char] -= 1

    for key in freq_map.keys():
        if freq_map[key] != 0:
            return -1

    # Initialize two pointers
    i,j = 0,0
    moves = 0

    while i < len(str1) and j < len(str2):

        # If both chars are equal move both pointers ahead
        if str1[i] == str2[j]:
            i += 1
            j += 1
        
        # both char not equal move i till it's equal to j
        else:
            i += 1
            moves += 1
        
    return moves






























#taking inpit using fast I/O
def takeInput() :
    str1 = input().strip()
    str2 = input().strip()
    
    return str1, str2


#main
t = int(input().strip())
for i in range(t) :

    str1, str2 = takeInput()
    print(minCostToGivenString(str1,str2))