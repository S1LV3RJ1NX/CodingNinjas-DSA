# Ref: https://leetcode.com/problems/multiply-strings/discuss/1233171/Simple-multiplication-algorithm-in-Python

def multiplyStrings(n1, n2):
    len_n1 = len(n1)
    len_n2 = len(n2)
    prod = 0

    for jdx, char2 in enumerate(n2):
        intermediate_prod = 0
        dig2 = ord(char2) - ord('0')
        for idx, char1 in enumerate(n1):
            dig1 = ord(char1) - ord('0')
            intermediate_prod += dig1 * dig2 * 10**(len_n1-idx-1)
        prod += intermediate_prod * 10**(len_n2-jdx-1)

    return str(prod)

tc = int(input())

for _ in range(tc):
    a = input().strip()
    b = input().strip()
    ans = multiplyStrings(a,b)
    print(ans)