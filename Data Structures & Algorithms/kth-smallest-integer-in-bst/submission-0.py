# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        
        while curr or stack:
            # 1. Reach the leftmost node of the current subtree
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 2. Process the node
            curr = stack.pop()
            k -= 1
            
            # 3. If k reaches 0, we found our target
            if k == 0:
                return curr.val
            
            # 4. Move to the right subtree
            curr = curr.right