class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr = sorted((value, index) for index, value in enumerate(nums))
       
        left = 0
        right = len(arr) - 1

        while left < right:
            sum = arr[left][0] + arr[right][0]
            
            if sum == target:
                return sorted([arr[left][1], arr[right][1]]) 
            elif sum > target:
                right -= 1
            else:
                left += 1