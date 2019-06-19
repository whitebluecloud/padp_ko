import unittest


class FiboFrogTest(unittest.TestCase):
    def test_big_range(self):
        # N is an integer within the range [0..100,000];
        # each element of array A is an integer that can have one of the following values: 0, 1.
        self.assertEqual(solution([0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]), 3)


def solution(A):
    if len(A) <= 2:
        return 1

    # Initialize Arrays
    A.insert(0, 1)
    A.append(1)

    def fibo(m):
        # 피보나치를 각각 구하지 않고 저장한 데이터에서 뽑아온다 (Dynamic Programming)
        ret = [0, 1]
        for i in range(2, m):
            val = ret[i-1] + ret[i-2]
            if val >= m:
                break
            else:
                ret.append(val)
        return ret


    # 뛸 수 있는 수를 만든다
    fibo_arr = fibo(len(A))

    def find_max(T):
        r_list = list()
        for i, v in enumerate(T):
            if v == 1 and i in fibo_arr:
                r_list.append(i)
        return max(r_list)

    jumps = []

    while sum(jumps) < len(A) - 1:
        jumps.append(find_max(A[sum(jumps):]))

    if len(jumps) > 0:
        return len(jumps)

    return -1



if __name__ == '__main__':
    unittest.main()
