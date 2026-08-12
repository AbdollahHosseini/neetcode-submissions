class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for i in range(len(temperatures))]
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                _, stackInd = stack.pop()
                result[stackInd] = (i - stackInd)
            stack.append([t, i])
        
        return result
                
