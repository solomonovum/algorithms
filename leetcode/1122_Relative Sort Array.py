import unittest
from typing import List
from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if not self.exceptionHandling(arr1, arr2):
            return []

        dict_to_sort = {x: 0 for x in arr2}

        for x in arr1:
            if x in dict_to_sort.keys():
                count = dict_to_sort[x]
                dict_to_sort[x] = count + 1

        res = []
        for x, y in dict_to_sort.items():
            res.extend([x] * y)

        arr1_cn = Counter(arr1) - Counter(res)

        return res + sorted(arr1_cn.elements())


    def exceptionHandling(self, arr1: List[int], arr2: List[int]) -> bool:
        arr1_length = len(arr1)
        arr2_length = len(arr2)

        if arr1_length > 1000 or arr2_length > 1000:
            return False

        for x in arr1:
            if 0 > x or x > 1000:
                return False

        for x in arr2:
            if 0 > x or x > 1000:
                return False

        if arr2_length != len(set(arr2)):
            return False

        for x in arr2:
            if x not in arr1:
                return False

        return True


class TestStringMethods(unittest.TestCase):
    def test_case_a(self):
        arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
        arr2 = [2, 1, 4, 3, 9, 6]

        output = [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]

        sol = Solution()

        self.assertEqual(sol.relativeSortArray(arr1, arr2), output)

    def test_case_b(self):
        arr1 = [0, 1, 44, 0, 2, 53, 6, 8, 1, 7, 17, 8, 7, 7]
        arr2 = [7, 8, 1, 6, 2, 0]

        output = [7, 7, 7, 8, 8, 1, 1, 6, 2, 0, 0, 17, 44, 53]

        sol = Solution()

        self.assertEqual(sol.relativeSortArray(arr1, arr2), output)

    def test_case_c(self):
        arr1 = [2, 21, 43, 38, 0, 42, 33, 7, 24, 13, 12, 27, 12, 24, 5, 23, 29, 48, 30, 31]

        arr2 = [2, 42, 38, 0, 43, 21]

        output = [2, 42, 38, 0, 43, 21, 5, 7, 12, 12, 13, 23, 24, 24, 27, 29, 30, 31, 33, 48]

        sol = Solution()

        self.assertEqual(sol.relativeSortArray(arr1, arr2), output)


if __name__ == '__main__':
    unittest.main()
