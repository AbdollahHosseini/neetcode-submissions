class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = -1

        for l in range(len(heights) - 1):
            r = len(heights) - 1
            while l < r:

                if heights[l] > heights[r]:
                    cons = heights[r]
                else: cons = heights[l]
                
                size = cons * (r - l)

                if size > max:
                    max = size

                r -= 1
        
        return max
