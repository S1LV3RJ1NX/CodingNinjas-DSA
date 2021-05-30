from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)
def kThCharaterOfDecryptedString(s, k) :

    
    decrypted_str = ""
    i = 0
    l = len(s)

    while i < l:

        temp_str = ""
        freq = 0

        # char in string
        while i < l and ord('a') <= ord(s[i]) and ord(s[i]) <= ord('z'):
            temp_str += s[i] 
            i += 1

        # digits in string
        while i < l and ord('0') <= ord(s[i]) and ord(s[i]) <= ord('9'):
            freq = freq*10 + (ord(s[i]) - ord('0')) 
            i += 1


        decrypted_str += (temp_str*freq)

    # print(decrypted_str)

    len_dec = len(decrypted_str)

    if len_dec > 0 and k-1 < len_dec:
        # k is one based but our string is 0 based indexing
        return decrypted_str[k-1]
    
    return '$'

#taking inpit using fast I/O
def takeInput() :
    
    str1 = input().strip()
    k = int(input().strip())

    return str1, k

#main
str1, k = takeInput()
print(kThCharaterOfDecryptedString(str1, k))
