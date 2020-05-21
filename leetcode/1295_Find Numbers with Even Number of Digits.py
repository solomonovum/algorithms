import unittest
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        if not self.exceptionHandling(nums):
            return 0

        res = [x for x in nums if (len(str(x)) % 2) == 0]

        return len(res)

    def exceptionHandling(nums: List[int]) -> bool:
        length = len(nums)

        if 1 > length or length > 500:
            return False

        for x in nums:
            if 0 > x or x > 10 ** 5:
                return False

        return True


class TestStringMethods(unittest.TestCase):
    def test_case_a(self):
        nums = [12, 345, 2, 6, 7896]
        output = 2
        sol = Solution()

        self.assertEqual(sol.findNumbers(nums), output)

    def test_case_b(self):
        nums = [555, 901, 482, 1771]
        output = 1
        sol = Solution()

        self.assertEqual(sol.findNumbers(nums), output)


if __name__ == '__main__':
    unittest.main()
