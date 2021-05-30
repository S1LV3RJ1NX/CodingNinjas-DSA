from collections import deque

def minimumParentheses(pattern):

    stack = deque()

    for bracket in pattern:

        # if opening bracket add to stack
        if bracket == '(':
            stack.append(bracket)

        # if closing bracket and top is an opening bracket 
        # cancel it with the top
        elif bracket == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            # if closing bracket but no opening bracket 
            # present on stack append to stack
            else:
                stack.append(bracket)

    return len(stack)



tc = int(input())

for _ in range(tc):

    ip = input()
    print(minimumParentheses(ip))