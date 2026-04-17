# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def get_max_gain(node):
            if not node:
                return 0
            
            # 1. Recursively get the max gain from left and right subtrees
            # Use max(0, ...) to ignore paths that would decrease the total sum
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)
            
            # 2. Check the price of a path where the current node is the "highest" point
            current_path_sum = node.val + left_gain + right_gain
            
            # 3. Update the global maximum if this path is better
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # 4. Return the maximum gain this node can contribute to its parent
            # (A parent can only take one branch, not both)
            return node.val + max(left_gain, right_gain)

        get_max_gain(root)
        return self.max_sum
        