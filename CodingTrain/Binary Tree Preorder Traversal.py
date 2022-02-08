# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.visited_list = []
    
    def visit(self, node):
        self.visited_list.append(node.val)
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        #VLR
        if root is not None:
            self.visit(root)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        
        return self.visited_list