class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for n in tokens:
            if n=="+" :
                right=stack[-1]
                stack.pop()
                left=stack[-1]
                stack.pop()
                stack.append(int(left+right))
            elif n=="-":
                right=stack[-1]
                stack.pop()
                left=stack[-1]
                stack.pop()
                stack.append(int(left-right))
            elif n=="*":
                right=stack[-1]
                stack.pop()
                left=stack[-1]
                stack.pop()
                stack.append(int(left*right))
            elif n=="/":
                right=stack[-1]
                stack.pop()
                left=stack[-1]
                stack.pop()
                stack.append(int(left/right))
            else:
                stack.append(int(n))
        return stack[-1]