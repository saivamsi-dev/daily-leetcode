class Solution(object):
    def shortestSubstrings(self, arr):
        """
        :type arr: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict

        # Step 1: Count in how many distinct strings each substring appears
        sub_counts = defaultdict(int)
        
        for s in arr:
            # Collect unique substrings for the current string s
            seen_in_s = set()
            length = len(s)
            for i in range(length):
                for j in range(i + 1, length + 1):
                    seen_in_s.add(s[i:j])
            
            for sub in seen_in_s:
                sub_counts[sub] += 1
        
        # Step 2: Find the shortest & lexicographically smallest uncommon substring for each word
        ans = []
        for s in arr:
            candidates = []
            length = len(s)
            
            # Generate all substrings of s
            for i in range(length):
                for j in range(i + 1, length + 1):
                    sub = s[i:j]
                    # If substring appears ONLY in string s
                    if sub_counts[sub] == 1:
                        candidates.append(sub)
            
            if not candidates:
                ans.append("")
            else:
                # Sort by length first, then lexicographically
                candidates.sort(key=lambda x: (len(x), x))
                ans.append(candidates[0])
                
        return ans