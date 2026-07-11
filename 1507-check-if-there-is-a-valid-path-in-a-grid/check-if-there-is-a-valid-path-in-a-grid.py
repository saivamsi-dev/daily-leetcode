# from collections import deque

# class Solution(object):
#     def hasValidPath(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: bool
#         """
#         m, n = len(grid), len(grid[0])
        
#         # Mapping direction strings to coordinate offsets (dr, dc)
#         # and their exact opposites for connection validation.
#         dirs = {
#             "L": (0, -1, "R"),
#             "R": (0, 1, "L"),
#             "U": (-1, 0, "D"),
#             "D": (1, 0, "U")
#         }
        
#         # Mapping each street type to its two valid exit directions
#         streets = {
#             1: ["L", "R"],
#             2: ["U", "D"],
#             3: ["L", "D"],
#             4: ["R", "D"],
#             5: ["L", "U"],
#             6: ["R", "U"]
#         }
        
#         # BFS Queue initialization
#         queue = deque([(0, 0)])
#         visited = set([(0, 0)])
        
#         while queue:
#             r, c = queue.popleft()
            
#             # If we reached the destination, a valid path exists
#             if r == m - 1 and c == n - 1:
#                 return True
                
#             # Check all directions the current street cell can connect to
#             current_street = grid[r][c]
#             for direction in streets[current_street]:
#                 dr, dc, opposite_dir = dirs[direction]
#                 nr, nc = r + dr, c + dc
                
#                 # Check grid boundaries and if the neighbor is already visited
#                 if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
#                     neighbor_street = grid[nr][nc]
                    
#                     # The neighbor must have an opening facing back toward the current cell
#                     if opposite_dir in streets[neighbor_street]:
#                         visited.add((nr, nc))
#                         queue.append((nr, nc))
                        
#         return False


class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        visited = set([(0, 0)])
        
        # Helper function to check if cell (r1, c1) can transition to (r2, c2)
        def can_move(r1, c1, r2, c2):
            # Out of bounds check
            if not (0 <= r2 < m and 0 <= c2 < n):
                return False
                
            s1, s2 = grid[r1][c1], grid[r2][c2]
            
            # Case 1: Moving Right
            if r2 == r1 and c2 == c1 + 1:
                return s1 in [1, 4, 6] and s2 in [1, 3, 5]
            # Case 2: Moving Left
            if r2 == r1 and c2 == c1 - 1:
                return s1 in [1, 3, 5] and s2 in [1, 4, 6]
            # Case 3: Moving Down
            if r2 == r1 + 1 and c2 == c1:
                return s1 in [2, 3, 4] and s2 in [2, 5, 6]
            # Case 4: Moving Up
            if r2 == r1 - 1 and c2 == c1:
                return s1 in [2, 5, 6] and s2 in [2, 3, 4]
                
            return False

        # Simple DFS stack
        stack = [(0, 0)]
        
        while stack:
            r, c = stack.pop()
            
            if r == m - 1 and c == n - 1:
                return True
            
            # Check all 4 possible neighbor directions
            for nr, nc in [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]:
                if (nr, nc) not in visited and can_move(r, c, nr, nc):
                    visited.add((nr, nc))
                    stack.append((nr, nc))
                    
        return False