# https://www.codingninjas.com/codestudio/problem-details/max-product-count_763416
from collections import defaultdict

def maxProductCount(arr, n):

    product_freq_map = defaultdict(int)

    for i in range(n):
        for j in range(i+1,n):
            product_freq_map[arr[i]*arr[j]] += 1

    
    max_prod, max_freq = 0,0 

    for prod, freq in product_freq_map.items():
        if freq >= max_freq:
            # choose product with max freq but if multiple present
            # choose min among them
            if freq == max_freq:
                max_prod = min(max_prod, prod)
            else:
                max_prod = prod
                max_freq = freq

    # if there is no pair (product) having freq count > 1

    freq_ct = product_freq_map.get(max_prod,None)

    if freq_ct == None or freq_ct == 1:
        return[0]

    # if pair found we need nC2 = n*(n-1)/2
    return max_prod, (freq_ct * (freq_ct-1))//2



#Taking Inputs
t = int(input())
while t > 0:
    
    n = int(input())
    arr = [int(i) for i in input().split()][:n]
    
    print(*maxProductCount(arr, n))
    t -= 1
