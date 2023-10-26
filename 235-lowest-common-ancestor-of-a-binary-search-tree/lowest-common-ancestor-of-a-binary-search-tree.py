# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # left_root = 0
        # right_root = 0
        # while left_root != p and right_root != q:
        #     l, r = root.left, root.right
        #     left_root = l
        #     right_root = r
        
        #     print("root", root.val, "left", left_root.val, "right", right_root.val)
        #     if root.left and root.right != left_root or right_root:
        #         print("IDK")

        
        # # print(p, type(p)
        #     left_root = self.lowestCommonAncestor(root.left)
        #     right_root = self.lowestCommonAncestor(root.right)
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur