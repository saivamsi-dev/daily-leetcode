class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        size = 1 << n  # 2^n
        grid = [[0] * size for _ in range(size)]
        
        def fill(r: int, c: int, size: int, start_val: int):
            if size == 1:
                grid[r][c] = start_val
                return
            
            half = size // 2
            num_elements = half * half
            
            # Quadrants ordered by value range:
            # 1. Top-Right
            fill(r, c + half, half, start_val)
            # 2. Bottom-Right
            fill(r + half, c + half, half, start_val + num_elements)
            # 3. Bottom-Left
            fill(r + half, c, half, start_val + 2 * num_elements)
            # 4. Top-Left
            fill(r, c, half, start_val + 3 * num_elements)
            
        fill(0, 0, size, 0)
        return grid