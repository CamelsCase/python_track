# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_both(node):
            if node.val==p.val:
                return p
            elif node.val==q.val:
                return q
            elif node.val>p.val and node.val>q.val:
                return find_both(node.left)
            elif node.val<p.val and node.val<q.val:
                    return find_both(node.right)
            return node
        return find_both(root)
        