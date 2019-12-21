# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# queue 
# time: O(n), space: O(n)
from collections import deque
class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        depth = 0
        q = deque([root])
        while q:
            n = len(q)
            for i in range(n):
                out = q.popleft()
                if out.left is not None:
                    q.append(out.left)
                if out.right is not None:
                    q.append(out.right)
            depth += 1
        return depth

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
