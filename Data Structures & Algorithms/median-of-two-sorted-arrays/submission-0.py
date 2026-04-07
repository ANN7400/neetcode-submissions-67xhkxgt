class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array to optimize binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            partition1 = (low + high) // 2
            partition2 = (m + n + 1) // 2 - partition1
            
            # Edge cases: if partition is 0 or at the end of the array
            maxLeft1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
            minRight1 = nums1[partition1] if partition1 < m else float('inf')
            
            maxLeft2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
            minRight2 = nums2[partition2] if partition2 < n else float('inf')
            
            # Check if we found the correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Even number of elements
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                # Odd number of elements
                else:
                    return max(maxLeft1, maxLeft2)
            
            elif maxLeft1 > minRight2:
                # We are too far right in nums1, move left
                high = partition1 - 1
            else:
                # We are too far left in nums1, move right
                low = partition1 + 1