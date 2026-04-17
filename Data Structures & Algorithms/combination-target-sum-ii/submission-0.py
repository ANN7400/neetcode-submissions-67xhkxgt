class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort() # Sorting is essential for duplicate pruning

        def backtrack(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i == len(candidates):
                return

            # 1. Include candidates[i]
            cur.append(candidates[i])
            backtrack(i + 1, cur, total + candidates[i])
            cur.pop()

            # 2. Skip all duplicate values to avoid duplicate combinations
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            # 3. Exclude candidates[i] and move to the next unique number
            backtrack(i + 1, cur, total)

        backtrack(0, [], 0)
        return res