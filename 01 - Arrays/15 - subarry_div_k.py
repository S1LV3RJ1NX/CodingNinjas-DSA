# Ref: https://www.youtube.com/watch?v=QM0klnvTQzk&ab_channel=Pepcoding
def subArrayCount(arr, k):

    remainder_hash = {}
    remainder_hash[0] = 1
    sub_arr_ct = 0
    running_sum = 0

    for ele in arr:
        
        running_sum += ele
        rem = running_sum%k 
        value = remainder_hash.get(rem, None)
        if value:
            sub_arr_ct += value
            remainder_hash[rem] += 1
        else:
            remainder_hash[rem] = 1 

    return sub_arr_ct

tc = int(input())

for _ in range(tc):
    n,k = map(int, input().split())
    arr = [int(x) for x in input().split()]
    ans = subArrayCount(arr, k)
    print(ans)