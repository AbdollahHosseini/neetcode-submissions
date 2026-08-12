class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closers = {')': '(', '}': '{', ']': '['}

        if len(s) <= 1:
            return False

        for b in s:
            if b in closers.values():
                stack.append(b)
            else:
                if len(stack) >= 1 and closers[b] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return True