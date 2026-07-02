class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closers = {')': '(', '}': '{', ']': '['}

        for b in s:
            if b in closers:
                if stack and stack[-1] == closers[b]:
                    stack.pop()
                else: return False
            else: stack.append(b)

        return True if not stack else False