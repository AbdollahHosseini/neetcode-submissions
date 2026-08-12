class Solution:
    def search(self, nums: List[int], target: int) -> int:

        arr = nums

        while len(arr) > 1:
            n = len(arr) // 2

            if target == arr[n]:
                return n
            elif target < arr[n]:
                arr = arr[n:]
            else:
                arr = arr[:n]

        return arr.pop() if len(arr) > 1 else -1
