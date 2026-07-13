class Solution(object):
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1
            
        min_len = float('inf')
        left = 0
        current_or = 0
        bit_counts = [0] * 32
        
        for right in range(len(nums)):
            # Expand the window: Add right element's bits
            current_or |= nums[right]
            for i in range(32):
                if (nums[right] >> i) & 1:
                    bit_counts[i] += 1
            
            # Shrink the window: Process valid windows
            while current_or >= k and left <= right:
                min_len = min(min_len, right - left + 1)
                
                # Remove left element's bits on the fly
                for i in range(32):
                    if (nums[left] >> i) & 1:
                        bit_counts[i] -= 1
                        # If no other numbers in the window set this bit, clear it
                        if bit_counts[i] == 0:
                            current_or &= ~(1 << i)
                left += 1
                
        return min_len if min_len != float('inf') else -1