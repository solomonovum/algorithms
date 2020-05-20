import unittest
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        if not self.exceptionHandling(nums):
            return []

        # sort
        nums_copy = nums.copy()
        nums_copy.sort()

        # counting numbers
        cn = {x: 0 for x in nums_copy}

        for x in nums_copy:
            value = cn[x]
            if value >= 1:
                cn[x] = value + 1
            else:
                cn[x] = 1

        # set cumulative sum
        cs = {}
        sum = 0
        for x, y in cn.items():
            sum += y
            cs[x] = sum - y

        # call foreach
        res = [cs[x] for x in nums]

        return res

    def exceptionHandling(self, nums: List[int]) -> bool:
        length = len(nums)

        if 2 > length or length > 500:
            return False

        for x in nums:
            if 0 > x or x > 100:
                return False

        return True


class TestStringMethods(unittest.TestCase):
    def test_case_a(self):
        nums = [8, 1, 2, 2, 3]
        output = [4, 0, 1, 1, 3]
        sol = Solution()

        self.assertEqual(sol.smallerNumbersThanCurrent(nums), output)

    def test_case_b(self):
        nums = [6, 5, 4, 8]
        output = [2, 1, 0, 3]
        sol = Solution()

        self.assertEqual(sol.smallerNumbersThanCurrent(nums), output)

    def test_case_c(self):
        nums = [7, 7, 7, 7]
        output = [0, 0, 0, 0]
        sol = Solution()

        self.assertEqual(sol.smallerNumbersThanCurrent(nums), output)


if __name__ == '__main__':
    # nums = [8, 1, 2, 2, 3]
    # output = [4, 0, 1, 1, 3]
    # sol = Solution()
    #
    # ans = sol.smallerNumbersThanCurrent(nums)
    #
    # print(ans)

    unittest.main()

