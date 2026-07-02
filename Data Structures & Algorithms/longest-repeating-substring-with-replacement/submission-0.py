class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       
        maxF = 0
        count = {}

        for i in set(s):
            count[i] = 0

        l = 0
        r = 0

        result = 0

        while r < len(s):
            curr = s[r]
            count[curr] += 1
            maxF = max(count[curr], maxF)

            length = r - l + 1
            
            if k < (length - maxF):
                count[s[l]] -= 1
                l += 1
            else: result = max(result, length)

            r += 1

        return result
                
            
            



            
