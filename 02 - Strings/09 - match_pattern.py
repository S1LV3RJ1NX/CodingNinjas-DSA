from sys import stdin

def generate_hash(word):
    
    freq_dict = {}
    counter = 1
    word_hash = ""

    for char in word:
        if not freq_dict.get(char, None):
            freq_dict[char] = counter
            counter+=1
        word_hash += str(counter)
    return word_hash

def check_pattern(words, n, pattern):

    

    ans = list()
    pattern_hash = generate_hash(pattern)
    # print(pattern_hash)

    for word in words:
        word_hash = generate_hash(word)
        # print(pattern_hash, word_hash, word)
        if pattern_hash == word_hash:
            ans.append(word)
    
    return ans


tc = int(stdin.readline().strip())
for _ in range(tc):

    n = int(stdin.readline().strip())
    words = stdin.readline().split()
    pattern = stdin.readline().strip()

    matched_words = check_pattern(words, n, pattern)
    
    print(*matched_words)