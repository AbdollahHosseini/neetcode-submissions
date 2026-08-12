class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        m = (l + r) // 2
        if len(nums) >= 3:
            if nums[m] > nums[r]:
                if target > nums[r]:
                    r = m
                else:
                    l = m + 1
            elif nums[m] < nums[r]:
                if target > nums[r]:
                    r = m
                elif target > nums[m]:
                    l = m + 1
                else:
                    r = m
                    

        while l < r:
            m = (l + r) // 2

            if nums[m] > target:
                r = m
            else:
                l = m + 1

        return m if nums[m] == target else -1

