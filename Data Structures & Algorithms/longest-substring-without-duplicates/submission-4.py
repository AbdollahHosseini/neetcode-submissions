class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = 0

        if len(s) <= 1:
            return len(s)

        curr = ""

        for i in s:
            if i in curr:
                longest = max(len(curr), longest)
                curr = ""
            
            curr += i

        return longest



