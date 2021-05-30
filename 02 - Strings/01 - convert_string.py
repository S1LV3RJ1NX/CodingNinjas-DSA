tc = int(input())

for _ in range(tc):
   
    l = len(string)

    ans = ""
    ans += string[0].upper()

    for i in range(1, len(string)):
        if ans[-1] == ' ' and string[i] != ' ':
            ans += string[i].upper()
        
        else:
            ans += string[i]

    print(ans)