class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)
        values = []

        first = True
        count = 0
        before = -1

        for i in arr:

            if first:
                before = i
                count += 1
                first = False
    
            else:

                if i == (before + 1):
                    count += 1
                    before = i

                else:
                    values.append(count)
                    count = 1
                    before = i

        values.append(count)

        return max(values)
