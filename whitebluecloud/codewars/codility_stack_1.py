# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(S):
    s_len = len(S)

    if s_len == 0:
        return 1
    if s_len % 2 != 0 or S[0] not in '{([':
        return 0

    m = {
        '{': '}'
        , '}': '{'
        , '[': ']'
        , ']': '['
        , '(': ')'
        , ')': '('
    }
    stack = []
    result = 1

    for s in S:
        if s in '{([':
            stack.append(s)
        else:
            if len(stack) == 0 or s != m[stack.pop()]:
                result = 0
                break

    if len(stack) != 0:
        return 0

    return result