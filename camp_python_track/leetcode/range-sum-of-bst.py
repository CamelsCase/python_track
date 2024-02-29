# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sm = 0

        def pre_order(node):
            nonlocal sm
            if node:
                val = node.val
                if low<=val<=high:
                    sm+=val
                pre_order(node.left)
                pre_order(node.right)
        pre_order(root)
        return sm
