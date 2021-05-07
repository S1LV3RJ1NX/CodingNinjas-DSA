
from sys import stdin

def pairSum(arr, S):
    from collections import defaultdict

    hash_map = defaultdict(int)

    ans = []
    for ele in arr:

        other = S - ele
        present = hash_map.get(other, None)
        if present:
            if ele < other:
                # If multiple instances present add those many times
                for i in range(present):
                    ans.append([ele, other])
            else:
                for i in range(present):
                    ans.append([other, ele])
        
        hash_map[ele] += 1
        # print(hash_map, ele, ans)
    ans.sort(key= lambda x : x[0])
    # print(ans)
    return ans



# Main Code
n,S = list(map(int, stdin.readline().strip().split(" ")))
arr = list(map(int, stdin.readline().strip().split(" ")))
res = pairSum(arr, S)

for ele in res:
    print(*ele)
