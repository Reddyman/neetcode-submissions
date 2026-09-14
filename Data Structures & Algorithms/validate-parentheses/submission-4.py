class Solution:
    def isValid(self, s: str) -> bool:
        # push left bracks to stack
        # peek and pop if right bracket encountered
        # return true if stack is empty
        # O(n) time
        # O(n) space
        stack = []
        for c in s:
            if c == '[' or c == '(' or c == '{':
                stack.append(c)
                continue
            if len(stack) == 0: return False
            if c == ']' and stack[-1] == '[':
                stack.pop()
            elif c == '}' and stack[-1] == '{':
                stack.pop()
            elif c == ')' and stack[-1] == '(':
                stack.pop()
            else:
                return False
        return len(stack) == 0

        