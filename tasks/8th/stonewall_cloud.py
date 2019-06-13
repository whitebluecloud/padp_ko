# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(H):
    if H is None or len(H) == 0:
        return 0

    cnt = 0
    stack = []
    for i, h in enumerate(H):
        if len(stack) == 0 or stack[-1] < h:
            stack.append(h)
            cnt += 1
            continue

        while len(stack) != 0 and stack[-1] > h:
            stack.pop()

        if len(stack) == 0 or stack[-1] < h:
            stack.append(h)
            cnt += 1

    return cnt