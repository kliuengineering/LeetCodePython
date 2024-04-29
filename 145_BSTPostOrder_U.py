from typing import List, Optional, Dict, Set

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Bad solution -> O(V + E)
class Solution:
    # we must use [] for typing module elements
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def DFS(node: Optional[TreeNode], result: List[int]) -> None:
            if node != None:
                DFS(node.left, result)
                DFS(node.right, result)
                result.append(node.val)

        result = []
        DFS(root, result)
        return result
    

def main():
    nodeA = TreeNode(val=1)
    nodeB = TreeNode(val=2)
    nodeC = TreeNode(val=3)
    nodeD = TreeNode(val=4)
    nodeE = TreeNode(val=5)
    
    nodeA.right = nodeB
    nodeB.left = nodeC
    nodeB.right = nodeD
    nodeD.right = nodeE

    solution = Solution()
    print( solution.postorderTraversal(nodeA) )


if __name__ == "__main__":
    main()
