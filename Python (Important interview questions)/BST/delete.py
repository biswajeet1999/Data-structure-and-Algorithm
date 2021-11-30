# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getLargestNodeFromLeftSubTree(self, root):
        cur = root
        while cur.right:
            cur = cur.right
        return cur
            
    
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left and root.right:
                target = self.getLargestNodeFromLeftSubTree(root.left)
                root.val = target.val
                root.left = self.deleteNode(root.left, target.val)
            else:
                if root.right:
                    return root.right
                else:
                    return root.left
        return root