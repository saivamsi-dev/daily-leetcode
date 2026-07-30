class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        duplicates = []
        
        for num in nums:
            idx = abs(num) - 1
            
            # If the number at index `idx` is already negative, `num` is a duplicate
            if nums[idx] < 0:
                duplicates.append(abs(num))
            else:
                # Mark as visited by negating
                nums[idx] = -nums[idx]
                
        return duplicates