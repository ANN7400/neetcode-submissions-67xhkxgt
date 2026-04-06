class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n
        
        # Step 1: Calculate Prefix Products (Left to Right)
        # res[i] will store the product of all elements to the left of i
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        # Step 2: Calculate Suffix Products (Right to Left)
        # Multiply the existing prefix product by the product of all elements to the right
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res