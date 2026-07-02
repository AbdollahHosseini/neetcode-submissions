class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sS1 = sorted(s1)

        count = 0

        l = 0
        r = len(s1)

        while r < len(s2) + 1:
            curr = s2[l:r]

            if sS1 == sorted(curr):
                return True
            else:
                r += 1
                l += 1

        return False

