def solution(N):
    if N == 1:
        return get_round(1,1)
    if N == 2:
        return get_round(2,1)
    if N == 3:
        return get_round(3,2)
    pos_map = [-1] * 81
    pos_map[0] = 0
    pos_map[1] = 1
    res = get_pos(N, pos_map)

    return get_round(res, pos_map[N-1])

def get_pos(n, pos_map):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if pos_map[n] != -1:
        return pos_map[n]
    pos_map[n] = get_pos(n-1, pos_map) + get_pos(n-2, pos_map)
    return pos_map[n]

def get_round(a, b):
    return 2 * (a + b)


assert solution(1) == 4
assert solution(5) == 26
assert solution(6) == 42