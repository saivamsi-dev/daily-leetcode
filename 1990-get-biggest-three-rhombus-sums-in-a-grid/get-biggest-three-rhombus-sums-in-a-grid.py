class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sums = set()

        for r in range(m):
            for c in range(n):
                # Radius k = 0 (single cell)
                sums.add(grid[r][c])
                
                # Try all possible radii k > 0
                k = 1
                while r - k >= 0 and r + k < m and c - k >= 0 and c + k < n:
                    current_sum = 0
                    
                    # Top to Right
                    for i in range(k):
                        current_sum += grid[r - k + i][c + i]
                    # Right to Bottom
                    for i in range(k):
                        current_sum += grid[r + i][c + k - i]
                    # Bottom to Left
                    for i in range(k):
                        current_sum += grid[r + k - i][c - i]
                    # Left to Top
                    for i in range(k):
                        current_sum += grid[r - i][c - k + i]
                    
                    sums.add(current_sum)
                    k += 1

        return sorted(sums, reverse=True)[:3]