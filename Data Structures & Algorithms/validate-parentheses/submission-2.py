class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closers = {')': '(', '}': '{', ']': '['}

        for b in s:
            if b in closers.values():
                stack.append(b)
            else:
                if closers[b] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return True