class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        total_sum = 0
        n = len(arr)
        
        for i in range(n):
            # Calculate total subarrays that include arr[i]
            total_subarrays = (i + 1) * (n - i)
            
            # Count how many of those have an odd length
            odd_subarrays = (total_subarrays + 1) // 2
            
            # Add element's total contribution
            total_sum += odd_subarrays * arr[i]
            
        return total_sum