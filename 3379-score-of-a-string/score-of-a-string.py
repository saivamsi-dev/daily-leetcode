class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        _ord = ord
        _abs = abs
        
        for i in range(len(s) - 1):
            total += _abs(_ord(s[i]) - _ord(s[i + 1]))
            
        return total