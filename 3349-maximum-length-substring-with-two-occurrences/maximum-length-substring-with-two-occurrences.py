class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_len = 0
        n = len(s)
        
        k = 0  # Your starting index
        
        # We track counts of characters in our current window [k ... c]
        counts = {}
        
        for c in range(n):  # c grows and expands the substring
            char = s[c]
            counts[char] = counts.get(char, 0) + 1
            
            # If the count of the character we just added exceeds 2:
            # We move k forward and shrink the window until count <= 2
            while counts[char] > 2:
                left_char = s[k]
                counts[left_char] -= 1
                k += 1  # Increment k as you described!
            
            # Update maximum length found so far
            current_length = c - k + 1
            max_len = max(max_len, current_length)
            
        return max_len