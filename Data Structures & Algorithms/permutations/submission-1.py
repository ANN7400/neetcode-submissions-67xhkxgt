class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(current_path, used):
            # Base case: if the current path is the same length as nums, we found a permutation
            if len(current_path) == len(nums):
                result.append(list(current_path))
                return
            
            for i in range(len(nums)):
                # Skip the number if it's already in our current path
                if used[i]:
                    continue
                
                # 1. Choose the number
                used[i] = True
                current_path.append(nums[i])
                
                # 2. Explore further
                backtrack(current_path, used)
                
                # 3. Backtrack (undo the choice)
                current_path.pop()
                used[i] = False

        # Initialize the 'used' list with False for all elements
        backtrack([], [False] * len(nums))
        return result 