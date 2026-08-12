class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        product = 1
        zero = False
        for num in nums:
            if num == 0 and not zero:
                zero = not zero
                continue
            product *= num

        if zero:
            products = [0 if num != 0 else int(product) for num in nums]
        else:
            products = [int(product / num) if num != 0 else int(product / 1) for num in nums]
        return products

            