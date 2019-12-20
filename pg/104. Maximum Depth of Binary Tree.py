# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = []
        if root is not None:
            stack.append((1, root))
            
        depth = 0
        while stack != []:
            curtDepth, node = stack.pop()
            if node is not None:
                depth = max(curtDepth, depth)
                stack.append((curtDepth + 1, node.left))
                stack.append((curtDepth + 1, node.right))
        
        return depth
