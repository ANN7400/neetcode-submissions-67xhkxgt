class Solution:
    def findMin(self, nums: list[int]) -> int:
        # Initialize two pointers at the ends of the array
        low, high = 0, len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            
            # If the middle element is greater than the rightmost element,
            # the minimum MUST be in the right half (after the pivot).
            if nums[mid] > nums[high]:
                low = mid + 1
                
            # If the middle element is less than or equal to the rightmost,
            # the minimum is either 'mid' itself or to the left.
            else:
                high = mid
        
        # When low == high, we've found the smallest element
        return nums[low]