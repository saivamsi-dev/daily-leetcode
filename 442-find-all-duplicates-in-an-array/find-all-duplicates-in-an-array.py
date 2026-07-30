class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        duplicates = []
        _abs = abs  # Local function lookup optimization
        
        for x in nums:
            val = _abs(x)
            idx = val - 1
            
            # If the value at target index is negative, val is a duplicate
            if nums[idx] < 0:
                duplicates.append(val)
            else:
                # Mark target index as visited by negating it
                nums[idx] = -nums[idx]
                
        return duplicates