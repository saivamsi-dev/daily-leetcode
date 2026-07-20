class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :type rtype: bool
        """
        # Sort the asteroids to greedily destroy the smallest ones first
        asteroids.sort()
        
        for asteroid in asteroids:
            if mass >= asteroid:
                mass += asteroid
            else:
                return False
                
        return True