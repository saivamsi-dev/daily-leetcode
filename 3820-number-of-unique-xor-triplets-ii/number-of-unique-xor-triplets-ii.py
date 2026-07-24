class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        U = list(set(nums))
        n = len(U)
        
        # Step 1: Compute all unique pair XOR results
        pair_xors = set()
        for i in range(n):
            for j in range(i, n):
                pair_xors.add(U[i] ^ U[j])
        
        # Step 2: Compute all unique triplet XOR results
        triplet_xors = set()
        for p in pair_xors:
            for x in U:
                triplet_xors.add(p ^ x)
                
        return len(triplet_xors)