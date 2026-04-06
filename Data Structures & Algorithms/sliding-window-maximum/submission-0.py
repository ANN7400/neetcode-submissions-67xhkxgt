class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        dq = deque() # Stores indices
        res = []
        
        for i in range(len(nums)):
            # 1. Remove indices that are out of the current window range
            if dq and dq[0] == i - k:
                dq.popleft()
                
            # 2. Remove indices of elements smaller than the current element
            # (They can't be the maximum if nums[i] is present)
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
                
            dq.append(i)
            
            # 3. Add to results once we've reached the first full window
            if i >= k - 1:
                res.append(nums[dq[0]])
                
        return res