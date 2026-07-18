class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # The expected maximum element 'n' based on the array length
        n = len(nums) - 1
        
        # 'base[n]' must have a length of at least 2 (i.e., base[1] = [1, 1])
        if n < 1:
            return False
            
        # Construct the expected base[n] array
        expected = list(range(1, n)) + [n, n]
        
        # Sort the input array and check if it matches the expected permutation
        return sorted(nums) == expected