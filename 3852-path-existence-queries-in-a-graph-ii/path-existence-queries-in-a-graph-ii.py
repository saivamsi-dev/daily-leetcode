class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        # Step 1: Pair each value with its original index and sort by value
        sorted_nodes = sorted([(nums[i], i) for i in range(n)])
        
        # Original index to sorted position mapping
        pos = [0] * n
        for sorted_idx, (val, orig_idx) in enumerate(sorted_nodes):
            pos[orig_idx] = sorted_idx
            
        # Step 2: For each sorted index, find the furthest index it can reach to the right
        # and precompute component checks (if there's a gap > maxDiff, they are disconnected)
        nxt = [i for i in range(n)]
        comp = [0] * n
        curr_comp = 0
        
        right = 0
        for left in range(n):
            if left > 0 and sorted_nodes[left][0] - sorted_nodes[left - 1][0] > maxDiff:
                curr_comp += 1
            comp[left] = curr_comp
            
            while right + 1 < n and sorted_nodes[right + 1][0] - sorted_nodes[left][0] <= maxDiff:
                right += 1
            nxt[left] = right

        # Step 3: Initialize Binary Lifting table
        # LOG = 18 is enough since n <= 10^5 (2^17 = 131072)
        LOG = 18
        up = [[0] * LOG for _ in range(n)]
        
        for i in range(n):
            up[i][0] = nxt[i]
            
        for j in range(1, LOG):
            for i in range(n):
                up[i][j] = up[up[i][j - 1]][j - 1]
                
        # Step 4: Answer queries
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            p_u, p_v = pos[u], pos[v]
            # Ensure p_u is the smaller index
            if p_u > p_v:
                p_u, p_v = p_v, p_u
                
            # If they are in different components, no path exists
            if comp[p_u] != comp[p_v]:
                ans.append(-1)
                continue
                
            # Count the steps using binary lifting
            steps = 0
            curr = p_u
            for j in range(LOG - 1, -1, -1):
                if up[curr][j] < p_v:
                    curr = up[curr][j]
                    steps += (1 << j)
            
            # One final jump is needed to reach or overshoot p_v
            ans.append(steps + 1)
            
        return ans