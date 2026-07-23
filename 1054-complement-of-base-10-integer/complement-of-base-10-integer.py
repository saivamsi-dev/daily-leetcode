class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
            
        # Create a bitmask of 1s with the same bit length as n
        mask = (1 << n.bit_length()) - 1
        
        # XOR n with the mask to flip all bits
        return n ^ mask