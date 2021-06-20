
def isSubSequence(str1, str2):

    i = 0
    j = 0

    # iterate over str2 until we match each and every char of str1
    # loops ends if str2 ends before str1 or not all chars of str1 are traversed

    l1, l2 = len(str1), len(str2)

    while i<l1 and j<l2:
        if str1[i] == str2[j]:
            i += 1
            j += 1
        else:
            j += 1

    if i!= l1:
        return False
    
    return True


tc = int(input())

for _ in range(tc):
    s1 = input().strip()
    s2 = input().strip()
    print(isSubSequence(s1, s2))