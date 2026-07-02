class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0 for i in range(len(temperatures))]

        for temp in range(len(temperatures)):
            for other in range(temp, (len(temperatures))):
                if temperatures[temp] < temperatures[other]:
                    if stack[temp] == 0: stack[temp] = other - temp

        return stack
                
