def findNonRepeating(string):
    
    char_hash = [0]*26

    for char in string:
        char_hash[ord(char)-ord('a')]+=1

    for char in string:
        if char_hash[ord(char)-ord('a')] == 1:
            return char
    return '#'


tc = int(input())

for _ in range(tc):
    string = input().strip()
    ans = findNonRepeating(string)
    print(ans)