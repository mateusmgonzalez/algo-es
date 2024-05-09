
def valid_palindrome(word: str) -> bool:
    letras = ""
    for char in word:
        if char.isalnum():
            letras += char

    return letras.capitalize() == letras[::-1].capitalize()


def is_balanced(expression):
    stack = []
    for char in expression:
        if char in ['(', '[', '{']:
            stack.append(char)
        else:
            if not stack:
                return False
            top = stack.pop()
            if (char == ')' and top != '(') or (char == ']' and top != '[') or (char == '}' and top != '{'):
                return False
    return not stack





if __name__ == "__main__":
    expression = input().strip()
    print(is_balanced(expression))
