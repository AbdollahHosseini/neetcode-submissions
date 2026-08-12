class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        m = 0

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                if target > nums[r]:
                    if target > nums[m]:
                        l = m + 1
                    else:
                        r = m
                else: l = m + 1
            elif nums[m] < nums[r]:
                if target > nums[r]:
                    r = m
                elif target > nums[m]:
                    l = m + 1
                else:
                    r = m
                        
        if nums[l] == target:
            return l
        else: return -1

