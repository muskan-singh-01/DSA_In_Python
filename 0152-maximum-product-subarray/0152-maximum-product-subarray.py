class Solution(object):
    def maxProduct(self, nums):
        max_product = nums[0]
        min_product = nums[0]

        result = nums[0]

        for i in range(1, len(nums)):

            curr = nums[i]

            temp_max = max(
                curr,
                curr * max_product,
                curr * min_product
            )

            temp_min = min(
                curr,
                curr * max_product,
                curr * min_product
            )

            max_product = temp_max
            min_product = temp_min

            result = max(result, max_product)
        return result
        