'''
We will keep a window that will keep a range of unique characters where the range is defined by start 
and end indices. Initially, both ‘start' and ‘end’ equal to zero denoting that we have only one character 
in the current window i.e the character at 0th index. Along with this, we will also keep a HashMap
to store the last occurrence of the characters. Now we will keep incrementing the ‘end’ to iterate on each 
character of the string.  

If the current character at the ‘end’ index is not present in the window we will simply update the ‘
start' to the maximum index possible index of ‘start’ or the last occurrence of the current character. 
Then we update the ‘maxLen’ and it gets updated if the range ('end' - ‘start’ - 1) is greater than ‘maxLen’. 

Then store the current index in the Map/HashMap as the current index will be the last occurrence of the 
character till current index iterated. Also, increment the ‘end’ by 1. Finally, Return ‘maxLen’.
'''


def lengthOfLongestSubstring(s):
    hashmap = dict()
    start, end = 0,0

    maxlen = 0
    n = len(s)

    while end < n:

        char = s[end]

        # current char in map move start to next position
        # we dont use get as get can return value 0
        # also repeating char can be one which is behind our current start 
        # hence we need the maxium start value
        if char in hashmap:
            start = max(start, hashmap[char]+1)

        # current char not in map update maxlen
        maxlen = max(maxlen, end-start+1)

        # add curr char idx to map
        hashmap[char] = end
        end += 1

    return maxlen



print(lengthOfLongestSubstring(input().strip()))