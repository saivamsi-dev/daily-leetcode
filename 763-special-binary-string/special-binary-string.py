class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = 0
        i = 0
        res = []
        
        for j, char in enumerate(s):
            if char == '1':
                count += 1
            else:
                count -= 1
            
            # When count hits 0, we found an independent special substring
            if count == 0:
                # Recursively solve the inner part of this substring
                inner_optimized = self.makeLargestSpecial(s[i + 1:j])
                # Wrap it back with the outer '1' and '0'
                res.append('1' + inner_optimized + '0')
                # Move the start pointer for the next substring
                i = j + 1
                
        # Sort the components in descending order to maximize lexicographical value
        res.sort(reverse=True)
        
        return "".join(res)