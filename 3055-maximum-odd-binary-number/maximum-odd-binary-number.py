# class Solution:
#     def maximumOddBinaryNumber(self, s: str) -> str:
#         # Count the number of '1's and '0's
#         ones = s.count('1')
#         zeros = s.count('0')
        
#         # Place (ones - 1) '1's at the beginning, followed by all '0's, and 1 '1' at the end
#         return '1' * (ones - 1) + '0' * zeros + '1'

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = 0
        for c in s:
            if c=='1':
                count+=1
        
        res = '1'*(count-1)+'0'*(len(s)-count)+'1'
        return res