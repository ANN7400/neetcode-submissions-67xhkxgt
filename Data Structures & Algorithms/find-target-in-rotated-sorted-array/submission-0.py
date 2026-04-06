class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
            
            # Identify which half is sorted
            # Case 1: Left half is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1 # Target is in the left sorted range
                else:
                    low = mid + 1  # Target must be in the right half
            
            # Case 2: Right half is sorted
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1  # Target is in the right sorted range
                else:
                    high = mid - 1 # Target must be in the left half
                    
        return -1