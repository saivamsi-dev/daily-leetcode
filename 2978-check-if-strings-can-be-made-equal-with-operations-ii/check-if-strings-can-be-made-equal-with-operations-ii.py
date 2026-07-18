class Solution(object):
    def checkStrings(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Separate even and odd index characters for s1
        s1_even = sorted(s1[0::2])
        s1_odd = sorted(s1[1::2])
        
        # Separate even and odd index characters for s2
        s2_even = sorted(s2[0::2])
        s2_odd = sorted(s2[1::2])
        
        # They can be made equal if both even sets and odd sets match perfectly
        return s1_even == s2_even and s1_odd == s2_odd