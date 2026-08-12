class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openers = ['(', '{', '[']
        closers = {')': 0, '}': 1, ']': 2}

        for l in s:
            if l in openers:
                stack.append(l)
            elif l in closers.keys():
                if stack[-1] == openers[closers[l]]:
                    stack.pop()
                else:
                    return False

        
        return True