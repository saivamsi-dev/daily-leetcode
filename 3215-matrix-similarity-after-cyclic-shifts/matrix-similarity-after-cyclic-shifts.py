class Solution(object):
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        m = len(mat)
        n = len(mat[0])
        
        # Reduce k to avoid redundant full rotations
        shift = k % n
        
        # If shift is 0, no change happens, so the matrix is always similar
        if shift == 0:
            return True
            
        for i in range(m):
            for j in range(n):
                if i % 2 == 0:
                    # Even-indexed rows: cyclically shifted to the left
                    if mat[i][j] != mat[i][(j + shift) % n]:
                        return False
                else:
                    # Odd-indexed rows: cyclically shifted to the right
                    if mat[i][j] != mat[i][(j - shift + n) % n]:
                        return False
                        
        return True