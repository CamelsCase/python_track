# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        inorder_list = []
        def inorder(node):
            if node:
                inorder(node.left)
                inorder_list.append(node.val)
                inorder(node.right)
        inorder(root)
        # print(inorder_list)
        freq = Counter(inorder_list).most_common()
        out = []
        # print(freq)
        for i in freq:
            # print(i[0],freq[0][1])
            if i[1]==freq[0][1]:
                out.append(i[0])
        # print(out)
        return out
        