def removeVowels(inputString):
    
    ans = ""
    vowels = "aeiouAEIOU"

    for char in inputString:
        if char in vowels:
            continue

        ans += char 

    return ans


tc = int(input())

for _ in range(tc):
    ip = input()
    print(removeVowels(ip))