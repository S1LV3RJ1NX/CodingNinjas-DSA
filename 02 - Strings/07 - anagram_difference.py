from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

from collections import defaultdict

def getMinimumAnagramDifference(str1, str2):
    # simple logic would be to create a freq map of all characters in str1
    # for each char in str2, if that char is present dec it's count in str1
    # if not present we would need this char for anagram hence manipulation required.
    freq_map_s1 = defaultdict(int)
    manipulations = 0

    for char in str1:
        freq_map_s1[char]+=1

    for char in str2:

        if freq_map_s1.get(char, None):

            if freq_map_s1[char] == 0:
                freq_map_s1.pop(char)
                manipulations += 1
            else:
                # reduce count
                freq_map_s1[char] -= 1
        else:
            manipulations += 1

    return manipulations
                


#   Fast input
def takeInput():

    str1 = stdin.readline().strip()
    str2 = stdin.readline().strip()

    return str1, str2


# main
T = int(stdin.readline().strip())
for i in range(T):
    str1, str2 = takeInput()
    ans = getMinimumAnagramDifference(str1, str2)
    print(ans)
