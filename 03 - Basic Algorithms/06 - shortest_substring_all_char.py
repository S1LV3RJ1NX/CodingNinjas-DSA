"""
In this problem we have to find a substring which has all chars distinct.

One method can be to generate all possible substrings and check with the hashmap
for distinctness. Tc: O(n^2), Sc: O(n)

One method to generate all possible substrings and to reduce TC is to use
sliding window approach. As most of the substrings generated are not valid
set thus by using sliding window we can generate substrings which satisfy the
constraints.

We shall maintain an array, which will keep count of freq of chars in string.
If at any time we encounter a char in window whose freq > 1 we begin the shrinking 
process else we calculate new window len.

Since we want shortest substring we can initialize len to length of string
once the window contains dist chars we check for repeating chars and begin to shrink.
"""

def shortestSubstring(s):

    distinct_chars_count = len(set(s))
    freq_map = [0]*26

    start = 0
    curr_distinct_chars = 0
    min_len = len(s)

    #  this will be start indx of our final substring
    window_start_idx = 0
    num_a = ord('a')

    for end in range(len(s)):
        freq_map[ord(s[end])-num_a] += 1

        # If freq is one, a distinct char is found
        if freq_map[ord(s[end])-num_a] == 1:
            curr_distinct_chars += 1

        if curr_distinct_chars == distinct_chars_count:

            # window shrinking
            while freq_map[ord(s[start]) - num_a] > 1:
                freq_map[ord(s[start]) - num_a] -= 1

                # move to next char in the string
                start += 1

            # now window contains no repeating char
            window_len = end - start + 1

            if min_len > window_len:
                min_len = window_len
                window_start_idx = start 

    return s[window_start_idx: window_start_idx+min_len]


tc = int(input())

for _ in range(tc):

    s = input().strip()
    print(shortestSubstring(s))
        



