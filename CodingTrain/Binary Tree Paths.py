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
