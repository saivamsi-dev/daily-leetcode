class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        total_len = n + m - 1
        
        # Step 1: Initialize the word and tracking array
        word = ['?'] * total_len
        fixed = [False] * total_len
        
        # Apply all 'T' constraints
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    pos = i + j
                    if word[pos] == '?' or word[pos] == str2[j]:
                        word[pos] = str2[j]
                        fixed[pos] = True
                    else:
                        # Conflict between overlapping 'T' constraints
                        return ""
        
        # Step 2: Fill remaining flexible positions with 'a'
        for i in range(total_len):
            if word[i] == '?':
                word[i] = 'a'
        
        # Helper to check if substring starting at i matches str2
        def matches(start_idx: int) -> bool:
            for j in range(m):
                if word[start_idx + j] != str2[j]:
                    return False
            return True

        # Step 3: Satisfy all 'F' constraints
        for i in range(n):
            if str1[i] == 'F':
                if matches(i):
                    # We must modify the rightmost non-fixed character in this window to break the match
                    changed = False
                    for j in range(m - 1, -1, -1):
                        pos = i + j
                        if not fixed[pos]:
                            word[pos] = 'b'
                            changed = True
                            break
                    
                    if not changed:
                        return ""
        
        return "".join(word)