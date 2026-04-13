# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # 1. The first element of preorder is always the root
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # 2. Find where the root is in the inorder list to split it
        mid = inorder.index(root_val)
        
        # 3. Recursively build the left and right subtrees
        # Left Inorder: inorder[:mid]
        # Left Preorder: preorder[1:mid+1]
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        
        # Right Inorder: inorder[mid+1:]
        # Right Preorder: preorder[mid+1:]
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        
        return root