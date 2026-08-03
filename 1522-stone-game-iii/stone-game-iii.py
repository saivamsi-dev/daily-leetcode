class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        
        # Traverse backward from the end of the array
        for i in range(n - 1, -1, -1):
            take = 0
            best = float('-inf')
            
            # Try taking 1, 2, or 3 stones
            for k in range(1, 4):
                if i + k <= n:
                    take += stoneValue[i + k - 1]
                    best = max(best, take - dp[i + k])
            
            dp[i] = best
        
        # Result depends on Alice's relative advantage from index 0
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"