class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask to handle negative numbers
        MASK = 0xFFFFFFFF
        MAX = 0x7FFFFFFF

        while b != 0:
            carry = ((a & b) << 1) & MASK
            a = (a ^ b) & MASK
            b = carry

        # If a is negative in 32-bit, convert to Python negative int
        return a if a <= MAX else ~(a ^ MASK)