import unittest


class Solution:
    def __init__(self):
        self.d = {'(': ')', '{': '}', '[': ']'}

    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if len(stack) > 0 and stack[-1] not in self.d.values() and self.d[stack[-1]] == ch:
                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0


class TestStringMethods(unittest.TestCase):
    def test_case_a(self):
        input = '()'
        sol = Solution()

        self.assertEqual(sol.isValid(input), True)

    def test_case_b(self):
        input = '()[]{}'
        sol = Solution()

        self.assertEqual(sol.isValid(input), True)

    def test_case_c(self):
        input = '(]'
        sol = Solution()

        self.assertEqual(sol.isValid(input), False)

    def test_case_d(self):
        input = '([)]'
        sol = Solution()

        self.assertEqual(sol.isValid(input), False)

    def test_case_e(self):
        input = '{[]}'
        sol = Solution()

        self.assertEqual(sol.isValid(input), True)

    def test_case_f(self):
        input = ']'
        sol = Solution()


if __name__ == '__main__':
    unittest.main()
