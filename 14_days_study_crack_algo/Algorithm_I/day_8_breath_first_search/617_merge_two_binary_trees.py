from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        1. Check if root1 is None
            If: return root2
        2. Check if root2 is None
            If: return root1
        3. Update the value of root1 to the sum of root1 and root2
        4. Recursively call the 'mergeTrees' function on the left and right subtrees of root1 and root2
        5. Return root1

        """
        if not root1:
            return root2

        if not root2:
            return root1

        root1.val += root2.val

        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1
