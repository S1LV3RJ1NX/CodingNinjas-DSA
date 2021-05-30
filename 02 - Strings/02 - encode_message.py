from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


def encode(message):

    l = len(message)
    ans = message[0]
    count = 1

    for i in range(1,l):
        if message[i] == ans[-1]:
            count += 1
        else:
            ans += str(count)+message[i]
            count = 1
                
    ans += str(count)
    return ans







   



#   Main
T = int(input().strip())
while T > 0:
    T -= 1
    message = stdin.readline().strip()
    print(encode(message))
