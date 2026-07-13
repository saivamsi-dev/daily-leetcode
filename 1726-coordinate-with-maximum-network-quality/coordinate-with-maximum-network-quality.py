import math

class Solution(object):
    def bestCoordinate(self, towers, radius):
        """
        :type towers: List[List[int]]
        :type radius: int
        :rtype: List[int]
        """
        max_quality = 0
        best_coord = [0, 0]
        
        # The constraints state that coordinates are between 0 and 50
        for x in range(51):
            for y in range(51):
                current_quality = 0
                
                for tx, ty, q in towers:
                    # Calculate Euclidean distance squared to avoid floating-point issues early on
                    dist_sq = (x - tx) ** 2 + (y - ty) ** 2
                    
                    # A tower is reachable if distance <= radius (or distance_sq <= radius^2)
                    if dist_sq <= radius ** 2:
                        d = math.sqrt(dist_sq)
                        current_quality += int(q // (1 + d))
                
                # Check if we found a strictly better network quality
                # Strict greater-than preserves the lexicographically smallest coordinate automatically
                if current_quality > max_quality:
                    max_quality = current_quality
                    best_coord = [x, y]
                    
        return best_coord