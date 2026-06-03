class Solution:
    def climbStairs(self, n: int) -> int: 
        if n <= 2:
            return n
            
        # base cases: 1 way for step 1, 2 ways for step 2
        one_step_behind = 2
        two_steps_behind = 1
        current = 0
        
        for i in range(3, n + 1):
            current = one_step_behind + two_steps_behind
            # Shift our variables forward for the next iteration
            two_steps_behind = one_step_behind
            one_step_behind = current
            
        return current