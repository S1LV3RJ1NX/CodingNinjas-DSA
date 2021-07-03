'''
Algo for clockwise:
- Find transpose
- Take every row and swap ele from either end

Algo for anticlockwise
- Find transpose
- Take every col and swap ele from either end
'''

def inplaceRotate(arr, n):

    # transpose
    # This code can be imagined as traversing along the diagonal
    # and swapping elements above and below the diagonal
    for i in range(n):
        for j in range(i):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    # Swap col ele - Anticlk rotn
    for i in range(n//2):
        for j in range(n):
            arr[i][j], arr[n-i-1][j] = arr[n-i-1][j], arr[i][j]

    # Swap row ele - Clk rotn
    # for i in range(n):
    #     for j in range(n//2):
    #         arr[i][j], arr[i][n-j-1] = arr[i][n-j-1], arr[i][j]
    return arr


for _ in range(int(input())):
    n = int(input())
    arr = [ [ int(x) for x in input().split()] for i in range(n) ]
    inplaceRotate(arr, n)
    print(arr)