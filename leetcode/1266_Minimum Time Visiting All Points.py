class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if not self.exceptionHandling(points):
            return 0

        stack = []
        sum = 0
        for i in points:
            stack.append(i)
            if len(stack) == 2:
                sum += max(abs(stack[0][0] - stack[1][0]), abs(stack[0][1] - stack[1][1]))
                del stack[0]

        return sum

    def exceptionHandling(self, points: List[List[int]]) -> bool:
        if len(points) < 1 or len(points) > 100:
            return False

        for i in points:
            if len(i) != 2:
                return False
            if i[0] < -1000 or i[1] > 1000:
                return False

        return True
