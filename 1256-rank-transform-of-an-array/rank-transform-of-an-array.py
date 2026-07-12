class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :soft: List[int]
        """
        # Step 1 & 2: Get sorted unique elements
        sorted_unique = sorted(list(set(arr)))
        
        # Step 3: Map each element to its rank (1-indexed)
        ranks = {num: rank + 1 for rank, num in enumerate(sorted_unique)}
        
        # Step 4: Transform the original array using the map
        return [ranks[num] for num in arr]