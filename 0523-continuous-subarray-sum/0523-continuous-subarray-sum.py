class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prefix_sum = 0
        seen = {0: -1}

        for i in range(len(nums)):

            prefix_sum += nums[i]

            remainder = prefix_sum % k if k != 0 else prefix_sum

            if remainder in seen:
                if i - seen[remainder] >= 2:
                    return True
            else:
                seen[remainder] = i

        return False