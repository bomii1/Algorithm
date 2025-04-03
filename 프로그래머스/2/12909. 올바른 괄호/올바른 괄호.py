def solution(s):
    stack = []

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if not stack:
                return False
            stack.pop()
    return True if not len(stack) else False
