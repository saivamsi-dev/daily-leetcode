from collections import defaultdict, Counter

class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        n = len(source)
        parent = list(range(n))
        
        # Find operation with path compression
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        # Union operation
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j

        # Group indices based on allowed swaps
        for u, v in allowedSwaps:
            union(u, v)
            
        # Group indices belonging to the same component
        components = defaultdict(list)
        for i in range(n):
            root = find(i)
            components[root].append(i)
            
        hamming_distance = 0
        
        # For each component, count how many elements can be successfully matched
        for root, indices in components.items():
            source_counts = Counter(source[i] for i in indices)
            target_counts = Counter(target[i] for i in indices)
            
            # Intersection count determines the number of matching positions
            matches = sum((source_counts & target_counts).values())
            
            # Unmatched elements in this component contribute to the distance
            hamming_distance += (len(indices) - matches)
            
        return hamming_distance