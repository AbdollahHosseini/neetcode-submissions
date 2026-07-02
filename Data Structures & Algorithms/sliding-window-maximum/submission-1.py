class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        x = len(nums)

        result = []
        
        for y in range(x - k + 1):
            l = y
            r = l + k

            arr = nums[l:r]
            result.append(max(arr))


        return result
