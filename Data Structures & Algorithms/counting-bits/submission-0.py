class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize the DP table with zeros
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # dp[i >> 1] is dp[i // 2]
            # i & 1 checks if the last bit is 1 (odd) or 0 (even)
            dp[i] = dp[i >> 1] + (i & 1)
            
        return dp