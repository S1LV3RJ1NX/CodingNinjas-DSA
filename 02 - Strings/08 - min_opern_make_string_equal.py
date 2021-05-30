# https://www.codingninjas.com/codestudio/problem-details/minimum-operations-to-make-strings-equal_840703
def minimumOperations(a, b):

    """ We are allowed to swap between { a[i],a[n-i-1],b[i],b[n-i-1] },
    thus what we can do is form groups of them and check if letters can be
    rearranged among themselves without replacement. Also since each group is
    independent of other, we can calculate the preprocessing moves separately
    for each group and add them all together to get total count. 
    
    Let's see the cases when we don't need any preprocessing(replacing with a char 
    which is not in the group).

    Since, index notation becomes lengthy let me mark them with variables:
    c1,c2,c3,c4 = a[i],a[n-i-1],b[i],b[n-i-1]

    1) If all chars are equal then no swap and no preprocessing
    2) If any 2 chars are equal (let's say c1,c3), we can replace c2 with value of c4,
        thus, only one preprocessing move.
    3) For all other cases we would need 2 processing moves.

    Also when the length of string is odd, we need to consider the middle char separately.
    if the middle chars of both strings are unequal, we would need an additional preprocessing
    move"""

    l1, l2 = len(a), len(b)

    if l1 != l2:
        return -1

    preprocessing_moves = 0

    # Run loop only till half of string as other half is already being considered
    # simultaneouly as n-i-1
    for i in range(l1//2):
        c1,c2,c3,c4 = a[i], a[l1-i-1], b[i], b[l1-i-1]

        # no preprocessing
        if ((c1==c2)and(c3==c4)) or ((c1==c3)and(c2==c4)) or ((c1==c4)and(c2==c3)):
            continue
        
        # 1 preprocessing
        elif (c1==c3) or (c1==c4) or (c2==c3) or (c2==c4) or (c3==c4):
            preprocessing_moves += 1

        else:
            preprocessing_moves += 2

    # odd length and mid char is not equal
    if l1&1 and a[l1//2] != b[l2//2]:
        preprocessing_moves += 1
    
    return preprocessing_moves

# Main Code

t = int(input().strip())

for i in range(t):

    str_a = input().strip()
    str_b = input().strip()

    print(minimumOperations(str_a, str_b))
