class Solution(object):
    def maximumSaleItems(self, items, budget):
        """
        :type items: List[List[int]]
        :type budget: int
        :rtype: int
        """
        dp = [0] * (budget + 1)
        min_price = float('inf')
        
        # 0-1 Knapsack for first-time purchases
        for factor, price in items:
            min_price = min(min_price, price)
            
            # Count free items obtained when purchasing item 'i' for the first time
            # 1 (purchased copy) + free copies where factor_j is divisible by factor
            gain = sum(1 for factor_j, _ in items if factor_j % factor == 0)
            
            # Traverse backwards to maintain 0-1 Knapsack property
            for b in range(budget, price - 1, -1):
                if dp[b - price] + gain > dp[b]:
                    dp[b] = dp[b - price] + gain
        
        # Combine DP results with greedy remaining budget spent on the cheapest item
        max_total_items = 0
        for spent in range(budget + 1):
            total = dp[spent] + (budget - spent) // min_price
            if total > max_total_items:
                max_total_items = total
                
        return max_total_items