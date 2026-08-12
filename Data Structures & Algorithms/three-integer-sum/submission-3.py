class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        arr = []

        for l in range(len(nums) - 2):
            m = l + 1
            r = len(nums) - 1
            while m < r:
                
                l_val = nums[l]
                m_val = nums[m]
                r_val = nums[r]

                sum = l_val + m_val + r_val

                if sum == 0:
                    arr.append([l_val, m_val, r_val])

                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                        
                elif sum < 0:
                    m += 1
                else:
                    r -= 1


        return arr