import unittest
from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        if not self.exceptionHandling(startTime, endTime, queryTime):
            return 0

        res = 0

        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                res += 1

        return res

    def exceptionHandling(self, startTime: List[int], endTime: List[int], queryTime: int) -> bool:
        if len(startTime) != len(endTime):
            return False

        if len(startTime) < 1 or len(startTime) > 100:
            return False

        if queryTime < 1 or queryTime > 1000:
            return False

        for i in range(len(startTime)):
            if startTime[i] > endTime[i]:
                return False

        return True


class TestStringMethods(unittest.TestCase):
    def test_case_a(self):
        startTime = [1, 2, 3]
        endTime = [3, 2, 7]
        queryTime = 4
        sol = Solution()

        output = 1

        self.assertEqual(sol.busyStudent(startTime, endTime, queryTime), output)

    def test_case_b(self):
        startTime = [4]
        endTime = [4]
        queryTime = 4
        sol = Solution()

        output = 1

        self.assertEqual(sol.busyStudent(startTime, endTime, queryTime), output)

    def test_case_c(self):
        startTime = [4]
        endTime = [4]
        queryTime = 5
        sol = Solution()

        output = 0

        self.assertEqual(sol.busyStudent(startTime, endTime, queryTime), output)

    def test_case_d(self):
        startTime = [1, 1, 1, 1]
        endTime = [1, 3, 2, 4]
        queryTime = 7
        sol = Solution()

        output = 0

        self.assertEqual(sol.busyStudent(startTime, endTime, queryTime), output)

    def test_case_e(self):
        startTime = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        endTime = [10, 10, 10, 10, 10, 10, 10, 10, 10]
        queryTime = 5
        sol = Solution()

        output = 5

        self.assertEqual(sol.busyStudent(startTime, endTime, queryTime), output)

    def test_case_f(self):
        startTime = [339, 241, 786, 873, 724, 531, 258, 115, 309, 989, 207, 286, 536, 492, 527, 772, 891, 450, 581, 251,
                     65, 855, 759, 795, 26, 72, 673]
        endTime = [959, 416, 832, 934, 942, 908, 581, 197, 874, 998, 579, 766, 819, 504, 721, 778, 926, 488, 802, 493,
                   85, 985, 764, 901, 546, 842, 768]
        queryTime = 708

        sol = Solution()

        output = 9

        self.assertEqual(sol.busyStudent(startTime, endTime, queryTime), output)


if __name__ == '__main__':
    unittest.main()
