import unittest

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):

        if not root:
            return root

        if root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        if not left:
            return right

        return left
        
    def permute(self, nums):
        n = len(nums)
        if n == 0:
            return []

        ret = []
        
        def backtrack(nums, p):
            if p == n:
                ret.append(nums.copy())

            for i in range(p, n + 1):
                nums[i], nums[p] = nums[p], nums[i]
                backtrack(nums, p + 1)
                nums[i], nums[p] = nums[p], nums[i]

        backtrack(nums, 0)

        return ret

    def permuteII(self, nums):
        """
        docstring
        """
        if not nums:
            return []

        n = len(nums)

        ret = []
        ans = []
        visited = [0] * n
        def backtrack(p):
            """
            docstring
            """
            if p == n:
                ret.append(ans.copy())
                return
            
            for i in range(n):
                if visited[i] == 1 or (i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == 0):
                    continue

                ans.append(nums[i])
                visited[i] = 1
                backtrack(p + 1)
                ans.pop()
                visited[i] = 0

        sorted(nums)

        backtrack(0)

        return ret

    def combine(self, n, k):
        ans = []
        ret = []

        def dfs(cur, n, k):
            if len(ans) + n - cur + 1 < k:
                return

            if len(ans) == k:
                ret.append(ans.copy())
                return

            ans.append(cur)
            dfs(cur + 1, n, k)
            ans.pop()
            dfs(cur + 1, n, k)

        dfs(1, n, k)

        return ret

    def buildTree(self, preorder, inorder):
        """
        前序遍历数组的第一个元素为树的根节点
        根节点在中序遍历数组中左边的部分为根节点的左子树，右边部分为右子树
        递归的在左右部分构建树

        构造中序遍历元素与索引的字典快速定位到中序遍历中的根节点
        """
        def _buildTree(preorderLeft, preorderRight, inorderLeft, inorderRight):
            if preorderLeft > preorderRight:
                return None

            preorderRootIndex = preorderLeft
            inorderRootIndex = index[preorder[preorderRootIndex]]

            sizeLeftSubtree = inorderRootIndex - inorderLeft

            root = TreeNode(preorder[preorderRootIndex])

            root.left = _buildTree(preorderLeft + 1, preorderLeft + sizeLeftSubtree, inorderLeft, inorderRootIndex - 1)
            root.right = _buildTree(preorderLeft + sizeLeftSubtree + 1, preorderRight, inorderRootIndex + 1, inorderRight)

            return root

        index = {element : i for i, element in enumerate(inorder)}

        return _buildTree(0, len(preorder) - 1, 0, len(inorder) - 1)

class Test(unittest.TestCase):
    """
    docstring
    """
    def testCombine(self):
        self.assertEqual(Solution().combine(4, 2), [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]])

if __name__ == "__main__":
    unittest.main()