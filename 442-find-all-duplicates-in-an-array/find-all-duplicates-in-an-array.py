class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        while i < len(nums):
            correct_idx = nums[i] - 1
            # Swap if the element is not at its correct position
            if nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1
                
        # Collect elements that are not in their correct positions
        return [nums[i] for i in range(len(nums)) if nums[i] != i + 1]