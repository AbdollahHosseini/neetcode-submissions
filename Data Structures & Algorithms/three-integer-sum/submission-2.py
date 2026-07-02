class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        l = 0
        

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
                    ans = [l_val, m_val, r_val]
                    if ans not in arr:
                        arr.append(ans)

                if sum < 0:
                    m += 1
                else:
                    r -= 1


        return arr