from sys import stdin
MOD = 1000000007

def getProductArrayExceptSelf(arr, n) :
    flag = False
    product = 1
    for ele in arr:
        if ele == 0:
            if flag == False:
                flag = True 
                continue
            else:
                # multiple 0 case
                product = 0
                break
        product = (product * ele)%MOD

    if flag == True:
        if product == 0:
            return [0]*n 
        else:
            val = product
            for i in range(n):
                if arr[i] == 0:
                    arr[i] = val
                else:
                    arr[i] = 0
    else:
        for i in range(n):
            arr[i] = (product// arr[i])
    return arr


def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n

def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ") 
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    product = getProductArrayExceptSelf(arr, n)
    printList(product, n)
    
    t -= 1