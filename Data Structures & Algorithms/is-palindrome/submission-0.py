class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i.isalnum()]
        count = len(s) - 1
        
        for i in s:
            if i == s[count]:
                count -= 1
            else:
                return False
        return True