class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        pushes = 0
        
        # 1st round (up to 8 letters -> 1 push each)
        if n <= 8:
            return n * 1
        pushes += 8 * 1
        n -= 8
        
        # 2nd round (up to 8 letters -> 2 pushes each)
        if n <= 8:
            return pushes + n * 2
        pushes += 8 * 2
        n -= 8
        
        # 3rd round (up to 8 letters -> 3 pushes each)
        if n <= 8:
            return pushes + n * 3
        pushes += 8 * 3
        n -= 8
        
        # 4th round (remaining letters -> 4 pushes each)
        return pushes + n * 4