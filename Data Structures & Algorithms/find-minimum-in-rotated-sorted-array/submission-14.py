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
            elif midpoint < nums[r] and nums[r] < nums[l]:
                l = mid
            elif midpoint < nums[l] and nums[l] > nums[r]:
                r = mid
            elif l == r:
                return midpoint
        

        return nums[mid]
            
                

    
            

        
