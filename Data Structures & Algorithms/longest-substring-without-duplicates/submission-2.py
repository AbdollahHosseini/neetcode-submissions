class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = 0

        if s == " ":
            return 1

        curr = ""

        for i in s:
            if i in curr:
                longest = max(len(curr), longest)
                curr = ""
            
            curr += i

        return longest



