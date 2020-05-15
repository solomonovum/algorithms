import unittest


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # check exception
        self.handleException(S, T)

        s_res = self.extractString(S)
        t_res = self.extractString(T)

        if s_res == t_res:
            return True
        else:
            return False

    def handleException(self, S: str, T: str) -> bool:
        # check string size
        if min(len(S), len(T)) < 1 or max(len(S), len(T)) > 200:
            return False

        # check case and # character
        if S.isupper() or T.isupper():
            return False

        return True

    def extractString(self, S: str) -> str:
        stack = []

        for ch in S:
            if ch == '#':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(ch)

        return ''.join(stack)


class TestStringMethods(unittest.TestCase):
    def test_case_a(self):
        S, T = 'ab#c', 'ad#c'
        sol = Solution()

        self.assertEqual(sol.backspaceCompare(S, T), True)

    def test_case_b(self):
        S, T = 'ab##', 'c#d#'
        sol = Solution()

        self.assertEqual(sol.backspaceCompare(S, T), True)

    def test_case_c(self):
        S, T = 'a##c', '#a#c'
        sol = Solution()

        self.assertEqual(sol.backspaceCompare(S, T), True)

    def test_case_d(self):
        S, T = 'a#c', 'b'
        sol = Solution()

        self.assertEqual(sol.backspaceCompare(S, T), False)

    def test_case_f(self):
        S, T = 'y#fo##f', 'y#f#o##f'
        sol = Solution()

        self.assertEqual(sol.backspaceCompare(S, T), True)


if __name__ == '__main__':
    unittest.main()

