class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = 0


        curr = ""

        for i in s:
            if i in curr:
                longest = max(len(curr), longest)
                curr = ""
            
            curr += i

        longest = max(len(curr), longest)

        return longest



