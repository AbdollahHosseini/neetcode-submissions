class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[l] < nums[r]:
                r = mid
            else: l = mid + 1

        if l == r:
            l -= 1

        if nums[l] < nums[r]:
            return nums[l]
        else: return nums[r]