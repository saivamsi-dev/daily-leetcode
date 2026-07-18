# class Solution(object):
#     def canReach(self, arr, start):
#         """
#         :type arr: List[int]
#         :type start: int
#         :rtype: bool
#         """
#         # Base case: Out of bounds or already visited
#         if start < 0 or start >= len(arr) or arr[start] < 0:
#             return False
        
#         # Target reached
#         if arr[start] == 0:
#             return True
        
#         # Mark the current index as visited by making the value negative
#         jump = arr[start]
#         arr[start] = -arr[start]
        
#         # Recursively check the right and left jumps
#         return self.canReach(arr, start + jump) or self.canReach(arr, start - jump)

from collections import deque
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        q=deque()
        q.append(start)
        while q:
            curr=q.popleft()
            
            if arr[curr]==0:
                return True
            if arr[curr]<0:
                continue
            jump=arr[curr]
            if curr+jump<len(arr):
                q.append(curr+jump)
            if curr-jump >=0:
                q.append(curr-jump)
            arr[curr]=-arr[curr]
        return False

        