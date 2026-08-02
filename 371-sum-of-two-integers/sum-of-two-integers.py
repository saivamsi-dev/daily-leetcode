class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            # XOR handles sum without carry; AND + left shift handles carry
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        # If a > MAX_INT, convert to negative signed 32-bit integer
        return a if a <= MAX_INT else ~(a ^ MASK)