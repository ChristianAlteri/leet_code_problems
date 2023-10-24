# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is not None:
            root.left, root.right = root.right, root.left

            self.invertTree(root.left)
            self.invertTree(root.right)
            print(root)
            return root
            # l = root.left
            # r = root.right
            # while l.val & r.val:
            #     first_node = root.val
            #     curr = l
            #     l = r
            #     r = curr
            #     r = l.right
            #     l = l.left
            #     print(l, r)
        # for i in root:
