# 子音から始まる
# 母音が二つ以上連続しない
# 子音が二つ以上連続しない

from collections import Counter

import math
import unittest


MOD = 10**9+7
vowels = ['A', 'O', 'I', 'E', 'U']


def solution(S: 'string') -> 'number':
    v_cnt = 0
    c_cnt = 0
    ans = 1
    c = Counter(list(S))
    for s in S:
        if s in vowels:
            v_cnt += 1
        else:
            c_cnt += 1
    if c_cnt - v_cnt == 1 or c_cnt - v_cnt == 0:
        ans *= math.factorial(c_cnt)
        ans *= math.factorial(v_cnt)
        for v in c.values():
            if v != 0:
                ans //= math.factorial(v)
        ans %= MOD
        return ans
    else:
        return 0


class TestAnagram(unittest.TestCase):

    def test_anagram(self):
        string = 'AABC'
        expected = 2
        actual = solution(string)
        self.assertEqual(expected, actual)

    def test_zero(self):
        zero = 'B'
        expected = 1
        actual = solution(zero)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
