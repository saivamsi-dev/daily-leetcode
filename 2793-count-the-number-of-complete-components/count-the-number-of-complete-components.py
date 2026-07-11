class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build adjacency list and compute degrees
        adj = {i: [] for i in range(n)}
        degree = [0] * n
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1
            
        visited = [False] * n
        complete_components_count = 0
        
        # Step 2: Traverse each component using DFS
        for i in range(n):
            if not visited[i]:
                component_nodes = []
                
                # Standard DFS to collect all nodes in the current component
                stack = [i]
                visited[i] = True
                
                while stack:
                    curr = stack.pop()
                    component_nodes.append(curr)
                    
                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)
                
                # Step 3: Check if the component is complete
                # Total number of vertices in this component
                v_count = len(component_nodes)
                is_complete = True
                
                for node in component_nodes:
                    if degree[node] != v_count - 1:
                        is_complete = False
                        break
                
                if is_complete:
                    complete_components_count += 1
                    
        return complete_components_count