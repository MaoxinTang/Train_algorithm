class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        #
        ## dfs recursive
        res = []
        def dfs(root,string):
            if not root: return
            if not (root.left or root.right):
                res.append(string+str(root.val))
            if root.left:
                dfs(root.left,string+str(root.val)+"->")
            if root.right:
                dfs(root.right,string+str(root.val)+"->")
        dfs(root,"")
        return res
dfs iterative:

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        #
        ## dfs iterative
        stack,res = [(root,"")],[]
        while stack:
            node,path = stack.pop()
            if not (node.left or node.right):
                res.append(path+str(node.val))
            if node.left:
                stack.append((node.left,path+str(node.val)+"->"))
            if node.right:
                stack.append((node.right,path+str(node.val)+"->"))
        return res

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        stk = [(root, str(root.val))]
        
        while stk:
            curr, path = stk.pop()
            if curr:
                if curr != root:   #since a path won't start with a '->', and we've already set the start of the path as str(root.val)
                    path += '->' + str(curr.val)
                if curr.right:
                    stk.append((curr.right, path))
                if curr.left:
                    stk.append((curr.left, path))
                if not curr.right and not curr.left: # end of the path
                    res.append(path)
        return res