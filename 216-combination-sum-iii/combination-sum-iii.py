class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        results = []
        
        def backtrack(start, path, target):
            # Base condition: if path length matches k
            if len(path) == k:
                if target == 0:
                    results.append(list(path))
                return
            
            # Try numbers from `start` to 9
            for i in range(start, 10):
                # Pruning: If the current number is greater than remaining target, stop early
                if i > target:
                    break
                
                path.append(i)
                backtrack(i + 1, path, target - i)
                path.pop()  # Backtrack
                
        backtrack(1, [], n)
        return results