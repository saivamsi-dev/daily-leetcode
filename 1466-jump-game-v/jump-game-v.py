class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        memo = {}
        
        def dfs(i: int) -> int:
            if i in memo:
                return memo[i]
            
            max_val = 1
            
            # 1. Jump to the right: i + 1, i + 2, ..., i + d
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[i] > arr[j]:
                    max_val = max(max_val, 1 + dfs(j))
                else:
                    # Cannot jump over/on an element >= arr[i]
                    break
                    
            # 2. Jump to the left: i - 1, i - 2, ..., i - d
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[i] > arr[j]:
                    max_val = max(max_val, 1 + dfs(j))
                else:
                    # Cannot jump over/on an element >= arr[i]
                    break
            
            memo[i] = max_val
            return max_val
        
        # We can start at any index, so take the maximum of all starting choices
        return max(dfs(i) for i in range(n))