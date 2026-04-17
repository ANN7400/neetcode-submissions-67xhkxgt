class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def backtrack(i, cur, total):
            # Base Case 1: Target reached
            if total == target:
                res.append(cur.copy())
                return
            
            # Base Case 2: Out of bounds or exceeded target
            if i >= len(candidates) or total > target:
                return

            # Choice 1: Include candidates[i]
            cur.append(candidates[i])
            backtrack(i, cur, total + candidates[i])
            
            # Choice 2: Exclude candidates[i] (Backtrack)
            cur.pop()
            backtrack(i + 1, cur, total)

        backtrack(0, [], 0)
        return res   