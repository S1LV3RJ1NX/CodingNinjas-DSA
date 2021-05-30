def compareVersions(a, b):
    arr1 = [int(x) for x in a.split('.')]
    arr2 = [int(x) for x in b.split('.')]

    l1,l2 = len(arr1), len(arr2)
    i=0

    while i<l1 and i<l2:

        if arr1[i] > arr2[i]:
            return 1
        elif arr1[i] < arr2[i]:
            return -1
        i+=1

    if i == l1:
        while i < l2:
            if arr2[i] > 0:
                return -1
            i += 1
    
    elif i == l2:
        while i < l1:
            if arr2[i] > 0:
                return 1
            i += 1
    return 0

tc = int(input())
for _ in range(tc):
    v1 = input().strip()
    v2 = input().strip()
    ans = compareVersions(v1, v2)
    print(ans)