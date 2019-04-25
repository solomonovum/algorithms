class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        # open or closed?
        stack = []
        ret = []
        for index, element in enumerate(S):
            if element is '(':
                stack.append((element, index))
            else:
                if len(stack) is 1:
                    # if closed, then insert inner element(s)
                    ret.append(S[stack[0][1]+1:index])
                stack.pop()
        
        # list to str
        return ''.join(ret)
