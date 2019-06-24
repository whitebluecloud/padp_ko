import unittest


class TileTest(unittest.TestCase):
    def test_tile(self):
        # 정답 테스트
        self.assertEqual(solution(5), 26)
        self.assertEqual(solution(6), 42)
        # 최대 성능?
        self.assertGreater(solution(80), solution(79))
        # Exception Test
        with self.assertRaises(BaseException):
            solution(81)


def solution(N):
    if N > 80:
        raise BaseException
    ret = [0, 1]
    for i in range(2, N + 1):
        val = ret[i - 1] + ret[i - 2]
        ret.append(val)
    return ret[-1] * 4 + ret[-2] * 2


unittest.main()
