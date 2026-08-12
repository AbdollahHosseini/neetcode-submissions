class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = 0

        while l < r:
            if numbers[l] + numbers[r] == target and l != r:
                return [l + 1, r + 1]
                break
            else: l += 1
        else:
            r += 1

        return [l + 1, r + 1]