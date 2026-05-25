class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping = {')': '(', '}': '{', ']': '['}
        top=-1
        for i in s:
            if len(s) == 1:
                return False
            elif (i == "(" or i == "[" or i=="{"):
                stack.append(i)
            elif not stack:
                return False
            else:
                if stack[-1] == mapping[i]:
                    stack.pop()
                else:
                    return False
        return not stack
        