class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = sorted(nums)
        values = []
        count = 0
        before = -1
        on_first = True
        for i in arr:
            if on_first:
                count += 1
                before = i
                on_first = False
            else:
                if i == (before + 1):
                    count += 1
                    before = i
                elif i == before:
                    continue
                else:
                    values.append(count)
                    count = 1
                    before = i

        values.append(count)

        return max(values)
