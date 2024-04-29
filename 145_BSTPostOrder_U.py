from typing import List, Optional, Dict, Set, tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def DFS(node: Optional[TreeNode], result: List[int]) -> None:
            if node != None:
                DFS(node.left, result)
                DFS(node.right, result)
                result.append(node.val)

        result = []
        DFS(root, result)
        return result
    
