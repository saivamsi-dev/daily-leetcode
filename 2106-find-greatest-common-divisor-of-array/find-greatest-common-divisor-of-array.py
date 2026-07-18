class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find the smallest and largest numbers
        mn = min(nums)
        mx = max(nums)
        
        # Euclidean algorithm to find GCD
        while mn:
            mx, mn = mn, mx % mn
            
        return mx