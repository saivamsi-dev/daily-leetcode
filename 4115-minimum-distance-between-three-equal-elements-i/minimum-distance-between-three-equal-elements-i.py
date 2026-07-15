from collections import defaultdict
import math

class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        # Group indices by their corresponding value
        num_to_indices = defaultdict(list)
        for index, val in enumerate(nums):
            num_to_indices[val].append(index)
            
        min_dist = math.inf
        
        # Check all values that appear at least 3 times
        for val, indices in num_to_indices.items():
            if len(indices) >= 3:
                # Check consecutive triplets
                for i in range(len(indices) - 2):
                    dist = 2 * (indices[i + 2] - indices[i])
                    if dist < min_dist:
                        min_dist = dist
                        
        return min_dist if min_dist != math.inf else -1