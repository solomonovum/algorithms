import unittest
from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        if not self.exceptionHandling(A):
            return [[]]

        # reverse
        for x in A:
            x.reverse()

        # invert
        for x in A:
            for y in range(len(x)):
                x[y] = x[y] ^ 1

        return A

    def exceptionHandling(self, A: List[List[int]]) -> bool:
        if len(A) < 1 or len(A[0]) > 20 or len(A) != len(A[0]):
            return False

        for x in A:
            for y in x:
                if y < 0 or y > 1:
                    return False

        return True


class TestStringMethods(unittest.TestCase):
    def test_case_a(self):
        input = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
        output = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]

        sol = Solution()

        self.assertEqual(sol.flipAndInvertImage(input), output)

    def test_case_b(self):
        input = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
        output = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]

        sol = Solution()

        self.assertEqual(sol.flipAndInvertImage(input), output)


if __name__ == '__main__':
    unittest.main()

