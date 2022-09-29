class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
 
class Solution:
    def depth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        return max(left_depth, right_depth) + 1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if abs(self.depth(root.left) - self.depth(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False
        
