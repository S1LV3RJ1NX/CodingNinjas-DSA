def leftRotate(strr,d):
    n = len(strr)

    return strr[d%n:]+strr[:d%n]

def rightRotate(strr,d):
    n = len(strr)
    d = n - (d%n)
    return strr[d:]+strr[:d]



tc = int(input())
for _ in range(tc):
    string = input()
    d = int(input())
    left = leftRotate(string, d)
    right = rightRotate(string, d)
    print(left, right)