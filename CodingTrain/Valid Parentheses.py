class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
                '{': '}',
                '(': ')',
                '[': ']'
            }
        for i in s:
            if(stack and match.get(stack[-1]) == i):
                stack.pop()
            else:
                stack.append(i)
        return(not bool(stack))