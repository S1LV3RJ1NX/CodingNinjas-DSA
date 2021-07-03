def rowWaveForm(mat):
    row = len(mat)
    ans = []

    for i in range(row):
        # odd row append in revserse
        if i&1:
            ans.extend(mat[i][::-1])
        else:
            ans.extend(mat[i])

    return ans 

for _ in range(int(input())):
    n , m = map(int, input().split())
    mat = [ [int(x) for x in input().split()] for i in range(n)]
    print(*rowWaveForm(mat))
