class Solution(object):
    def maximumSubarraySum(self, nums, k):

        freq = {}
        window_sum = 0
        max_sum = 0
        left = 0

        for right in range(len(nums)):

            # Add new element
            num = nums[right]
            freq[num] = freq.get(num, 0) + 1
            window_sum += num

            # Maintain window size k
            if right - left + 1 > k:
                old = nums[left]

                window_sum -= old
                freq[old] -= 1

                if freq[old] == 0:
                    del freq[old]

                left += 1

            # Check distinct elements
            if right - left + 1 == k:
                if len(freq) == k:
                    max_sum = max(max_sum, window_sum)

        return max_sum
            

        
        