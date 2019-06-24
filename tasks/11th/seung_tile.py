import unittest


class TileTest(unittest.TestCase):
    def test_ant(self):
        self.assertEqual(solution(5, 26))
        self.assertEqual(solution(6, 42))
        self.assertEqual(solution(81, None))


def solution(N):
    if N > 80:
        return
    ret = [0, 1]
    for i in range(2, N + 1):
        val = ret[i - 1] + ret[i - 2]
        ret.append(val)
    return ret[-1] * 4 + ret[-2] * 2
