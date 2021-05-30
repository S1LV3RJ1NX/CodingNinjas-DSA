from sys import stdin, stdout, setrecursionlimit
setrecursionlimit(10 ** 7)


def nextLargestPalindrome(S, length):


    array = [int(x) for x in S]
    # print(array)
    # If all 9's
    if S[0]=='9' and S[0]*length == S:
        return str(int(S)+2)

    # find mid idx, initialize i, j
    # to scan left and right sections of mid
    mid = length//2

    i = mid-1
    # if odd then mid+1 else mid
    j = mid+1 if (length&1) else mid

    # reach to the section which is not palindrome
    while (i>=0 and array[i]==array[j]):
        i-=1
        j+=1

    # A bool variable to check if copy of left side to right is sufficient or not
    leftsmaller = False

    # Find if middle array is incremented or not
    # or copying left side is not sufficient
    if ( i < 0 or array[i] < array[j]): 
        leftsmaller = True

    # copy left mirror to right
    while i>=0:
        array[j] = array[i]
        j+=1
        i-=1

    # Case where middle digit must be incremented
    if leftsmaller:
        carry = 1
        i = mid-1

        # if there are odd digits inc middle and store the carry 
        if length&1:
            array[mid] += 1
            carry = array[mid]//10
            array[mid] %= 10
            j = mid + 1
        else:
            j = mid 

        while (i >= 0) : 
            array[i] += carry 
            carry = array[i] // 10
            array[i] %= 10
            array[j] = array[i]  # copy mirror to right 
            j+=1
            i-=1
    return "".join(str(x) for x in array)



# Taking input using fast I/0
def takeInput():
    N = int(stdin.readline())
    S = stdin.readline().strip()
    return N, S


tc = int(input())
while tc > 0:
    N, S = takeInput()
    S = nextLargestPalindrome(S, N)
    stdout.write(S + "\n")
    tc -= 1