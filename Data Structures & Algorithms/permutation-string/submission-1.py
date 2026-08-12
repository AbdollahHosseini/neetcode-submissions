class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sumS1 = 0
        for i in s1:
            sumS1 += ord(i)

        count = 0

        l = 0
        r = len(s1)

        while r < len(s2):
            total = sum(ord(char) for char in s2[l:r])

            if sumS1 == total:
                return True
            else:
                r += 1
                l += 1

        return False

