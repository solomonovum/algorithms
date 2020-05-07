import unittest


class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for ch in S:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)


class TestStringMethods(unittest.TestCase):
    def test_case_a(self):
        input = 'aca'
        ans = 'aca'
        sol = Solution()
        self.assertEqual(sol.removeDuplicates(input), ans)

    def test_case_b(self):
        input = 'abbaca'
        ans = 'ca'
        sol = Solution()
        self.assertEqual(sol.removeDuplicates(input), ans)

    def test_case_c(self):
        input = 'abbbaca'
        ans = 'abaca'
        sol = Solution()
        self.assertEqual(sol.removeDuplicates(input), ans)

    def test_case_d(self):
        input = 'abbb'
        ans = 'ab'
        sol = Solution()
        self.assertEqual(sol.removeDuplicates(input), ans)

    def test_case_e(self):
        input = 'aaaaaaaaa'
        ans = 'a'
        sol = Solution()
        self.assertEqual(sol.removeDuplicates(input), ans)


if __name__ == '__main__':
    unittest.main()
