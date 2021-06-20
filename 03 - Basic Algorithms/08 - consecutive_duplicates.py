from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def removeConsecutiveDuplicates(str):
    ans = str[0]

    for char in str[1:]:
        if ans[-1] != char:
            ans += char
    
    return ans





# fast input
def takeInput() :
	string = stdin.readline().strip()

	return string
# Main
string = takeInput()
print(removeConsecutiveDuplicates(string))