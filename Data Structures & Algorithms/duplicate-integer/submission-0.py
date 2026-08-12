class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = ()
        for i in nums:
            if nums in seen:
                return true
            else:
                seen.add(i)
        
        return false