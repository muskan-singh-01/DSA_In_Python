
class Solution:
    def subarraysDivByK(self, nums, k):

        prefix = 0
        count = 0

        freq = {0: 1}

        for num in nums:

            prefix += num

            remainder = prefix % k

            if remainder in freq:
                count += freq[remainder]

            freq[remainder] = freq.get(remainder, 0) + 1

        return count
