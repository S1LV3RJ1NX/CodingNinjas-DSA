"""
Check from left to right and then check from right to left.
When check from left to right, take all '*'s as '(', to see whether can match all ')'s.
And, When check from right to left, take all '*'s as ')', to see whether can match all '('s.
If both checks are valid, then the string is valid.

Part one:
The first loop guarantees there would be no ) left for pairing, but there may be ( or * left.
if * left, we can use * as '', there is still a fully match.
To check if there are ( left, the second loop comes.

Part two:
the second loop guarantees there would be no ( left for pairing.

The Intersection of part one and part two guarantees there would be no ) and no ( left for pairing.
So this solution works well.
"""

def checkValidString(s):

    balance = 0
    l = len(s)

    # L2R Assume * is '('
    for i in range(l):
        if s[i] == '(' or s[i] == '*':
            balance += 1

        # We encounter ) but no '(' or '*' one to cancel it hence check balance 
        elif balance == 0:
            return False
        else:
            balance -= 1


    # once we come out of loop if we balance is 0 it means combn of ( and * cancel out
    if balance == 0:
        return True 

    balance = 0
    # R2L assume * is ')'
    for i in range(l-1,-1,-1):
        if s[i] == ')' or s[i] == '*':
            balance += 1

        # We encounter ( but no ')' or '*' one to cancel it hence check balance 
        elif balance == 0:
            return False
        else:
            balance -= 1
    
    return True


    

    


tc = int(input())

for _ in range(tc):
    string = input()
    if checkValidString(string):
        print("Yes")
    else:
        print("No")