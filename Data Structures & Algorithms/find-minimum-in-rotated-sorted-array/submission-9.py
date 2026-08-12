class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        mid = 0

        while l <= r:
            mid = (l + r) // 2
            midpoint = nums[mid]
    
            if midpoint > nums[r] and nums[r] < nums[l]:
                l = mid + 1
            elif midpoint > nums[l] and nums[r] > nums[l]:
                r = mid - 1
            elif midpoint < nums[l] and nums[r] < nums[l]:
                r = mid - 1
            else:
                return midpoint

        return nums[mid]
            
                

    
            

        
