def valid_parentheses(s):
    stack = []

    for par in s:
        print(stack)
        if par == '(' or par == '[' or par == '{':
            stack.append(par)

        elif par == ')' and stack and stack[-1] == '(':
            stack.pop()
        elif par == ']' and stack and stack[-1] == '[':
            stack.pop()
        elif par == '}' and stack and stack[-1] == '{':
            stack.pop()
        else:
            return False

    return not stack