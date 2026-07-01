class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for n in s:
            if not stack:
                stack.append(n)
            else:
                if n==")"and stack[-1]=="(":
                    stack.pop()
                elif n=="}"and stack[-1]=="{":
                    stack.pop()
                elif n=="]"and stack[-1]=="[":
                    stack.pop()
                else:
                    stack.append(n)
        if stack:
            return False
        return True
