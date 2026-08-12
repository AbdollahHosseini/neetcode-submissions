class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = "" 
        maximum = 0
        
        for letter in s:
            tmp = sub
            sub += letter
            while len(set(sub)) < len(sub):
                maximum = max(maximum, len(tmp))
                sub = sub[1:]
            
        return maximum