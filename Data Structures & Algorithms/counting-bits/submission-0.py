class Solution:
    def countBits(self, n: int) -> List[int]:
        count = [0 for i in range(n + 1)]
        for i in range(n + 1):
            count[i] += bin(i).count('1') 

        return count