class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, low, high):
            # An empty tree is a valid BST
            if not node:
                return True
            
            # The current node's value must be strictly between low and high
            if not (low < node.val < high):
                return False
            
            # 1. Left subtree: must be < current node value
            # 2. Right subtree: must be > current node value
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))
        
        # Initial boundaries are negative and positive infinity
        return validate(root, float('-inf'), float('inf'))