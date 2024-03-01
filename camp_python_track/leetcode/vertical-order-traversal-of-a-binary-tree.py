# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dt = defaultdict(list)
        def traverse(row,col,right,node):
            if node:
                dt[col].append((row,right,node.val))
                traverse(row+1,col-1,right-1,node.left)
                traverse(row+1,col+1,right+1,node.right)
        traverse(0,0,0,root)
        ls = []
        for i in sorted(dt.keys()):
            ans =  []
            for j in sorted(dt[i],key = lambda x: (x[0],x[1],x[2])):
                ans.append(j[2])
            ls.append(ans)
        return ls