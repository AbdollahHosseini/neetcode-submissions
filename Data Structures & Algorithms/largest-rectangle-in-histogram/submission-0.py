class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        result = 0

        for i, h in enumerate(heights + [0]):
            changeInd = i
            while stack and h < stack[-1][0]:
                stackHeight, stackInd = stack.pop()
                result = max(result, stackHeight * (i - stackInd))
                changeInd = stackInd
            
            stack.append([h, changeInd])

        return result


