from collections import defaultdict

def getLengthofLongestSubstring(k, s):

    # create a hash_map of all the char and their frequiency
    hash_map = defaultdict(int)    

    l = len(s)
    window_start = 0
    max_len = 0

    # i denotes window_end
    for i in range(l):

        # Generate window
        if not hash_map.get(s[i], None):
            # add element to map make it's freq as 1
            hash_map[s[i]] += 1
        else:
            # just increment the frequency
            hash_map[s[i]] += 1

        # if our hash_map has more than k keys it means
        # we have more than k distinct chars in our current window
        # hence we need to decrease the window size
        while len(hash_map) > k:
            # reduce the freq of char at start of window
            hash_map[s[window_start]] -= 1

            if hash_map.get(s[window_start], None) == 0:
                # freq becomes 0, remove that ele 
                hash_map.pop(s[window_start])
            # move to next ele by inc window_start 
            window_start += 1

        max_len = max(max_len, i-window_start+1)

    return max_len
            











tc = int(input())

for _ in range(tc):
    k = int(input())
    s = input()
    ans =  getLengthofLongestSubstring(k,s)
    print(ans)