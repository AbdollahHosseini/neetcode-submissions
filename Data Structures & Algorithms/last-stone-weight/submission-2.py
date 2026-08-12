class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = stones
        while len(stones) > 1:
            arr = sorted(stones)
            x = arr[-1]
            y = arr[-2]

            if x == y:
                arr.pop()
                arr.pop()
            elif x < y:
                arr[-2] = y - x
                arr.pop()
            else:
                arr[-2] = x - y
                arr.pop()
            stones = arr

        if not stones:
            return 0
        else: return stones[0]