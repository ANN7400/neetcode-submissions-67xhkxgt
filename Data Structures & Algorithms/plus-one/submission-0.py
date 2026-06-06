class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Traverse the array backwards
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits # No carry left, we can stop early!
            
            # If it was 9, it becomes 0, and loop continues to apply carry
            digits[i] = 0
            
        # If we exit the loop, it means all digits were 9 (e.g., [9, 9] -> [0, 0])
        # We need to insert a 1 at the beginning
        return [1] + digits
        