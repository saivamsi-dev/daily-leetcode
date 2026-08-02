class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        
        for c in s:
            if stack:
                prev = stack[-1]
                diff = abs(ord(c) - ord(prev))
                
                # Consecutive in circular alphabet if diff is 1 or 25 ('a' and 'z')
                if diff == 1 or diff == 25:
                    stack.pop()
                    continue
            
            stack.append(c)
            
        return "".join(stack)