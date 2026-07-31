from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count frequency of each character
        freqs = Counter(word).values()
        
        # Sort frequencies in descending order
        sorted_freqs = sorted(freqs, reverse=True)
        
        total_pushes = 0
        
        # Calculate minimum pushes using greedy approach
        for i, count in enumerate(sorted_freqs):
            pushes_needed = (i // 8) + 1
            total_pushes += count * pushes_needed
            
        return total_pushes