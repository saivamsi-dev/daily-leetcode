class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        total_elements = m * n
        
        # Optimize k if it's larger than the total number of elements
        k = k % total_elements
        
        # Create a new grid of the same dimensions filled with zeros
        result = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                # Calculate the 1D index and shift it
                old_1d_index = i * n + j
                new_1d_index = (old_1d_index + k) % total_elements
                
                # Convert back to 2D indices
                new_row = new_1d_index // n
                new_col = new_1d_index % n
                
                result[new_row][new_col] = grid[i][j]
                
        return result