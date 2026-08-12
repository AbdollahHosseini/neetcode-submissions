class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        begin = False

        while l < r:

            if nums[l] < nums[r]:
                begin = True
            else:
                begin = False

            mid = (l + r) // 2
            midpoint = nums[mid]
    
            leftM = nums[mid - 1]
            rightM = nums[mid + 1]

            if midpoint > rightM:
                return rightM
                break
            elif midpoint < leftM:
                return midpoint
                break
            elif midpoint > leftM and not begin:
                l = mid + 1
            elif midpoint > leftM and begin:
                r = mid - 1
            elif midpoint < rightM and not begin:
                l = mid + 1
            elif midpoint < rightM and begin:
                r = mid - 1
            
                

    
            

        
