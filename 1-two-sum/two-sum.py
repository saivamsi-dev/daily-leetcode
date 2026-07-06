class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i in range(len(nums)):
            c=target-nums[i]
            if c in d:
                return [d[c],i]
            d[nums[i]]=i 
        return [-1,-1]