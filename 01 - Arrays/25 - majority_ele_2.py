# https://leetcode.com/problems/majority-element-ii/discuss/63520/Boyer-Moore-Majority-Vote-algorithm-and-my-elaboration
# https://www.codingninjas.com/codestudio/problem-details/majority-element-ii_893027

    def majorityElementII(arr):
        # Write your code here.
        if not arr:
            return []

        ct1, ct2, candidate1, candidate2 = 0, 0, 0, 0

        for ele in arr:

            if ele == candidate1:
                ct1 += 1
            elif ele == candidate2:
                ct2 += 1
            elif ct1 == 0:
                candidate1 = ele 
                ct1 = 1
            elif ct2 == 0:
                candidate2 = ele 
                ct2 = 1
            else:
                ct1, ct2 = ct1-1, ct2-1
        
        l = len(arr)//3
        return [n for n in (candidate1, candidate2) 
            if arr.count(n) > l]

        
tc = int(input())

for _ in range(tc):
    n = input()
    arr = [int(x) for x in input().split()]
    sol = majorityElementII(arr)
    print(*sol)