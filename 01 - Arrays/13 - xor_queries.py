def xorQuery(queries):

    ans = []
    xor_val = 0

    for q_type, q_value in queries:
        if q_type == 1:
            # append element with running xor itself
            ans.append(q_value^xor_val)
        else:
            xor_val ^= q_value

    for i in range(len(ans)):
        ans[i] ^= xor_val
    return ans




q = int(input())
queries = [[int(x) for x in input().split()] for _ in range(q)]
ans = xorQuery(queries)
print(*ans)