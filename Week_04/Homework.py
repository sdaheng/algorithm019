import collections
import unittest
from typing import List

class Solution:
    # 搜索
    # 二分查找
    # flatten matrix
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0

        left = 0
        right = m * n - 1

        while left <= right:
            pivot = (left + right) // 2
            pivot_element = matrix[pivot // n][pivot % n]

            if pivot_element == target:
                return True
            else:
                if target > pivot_element:
                    left = pivot + 1
                else:
                    right = pivot - 1
        
        return False

    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, r, c):
            grid[r][c] = 0

            for x, y in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
                    dfs(grid, x, y)

        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    ret += 1
                    dfs(grid, i, j)
        
        return ret
        
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        nodes = dict()
        
        # 对单词进行编号作为图的节点
        def numberingWord(word):
            if word not in nodes:
                nonlocal nodeNums
                nodes[nodeNums] = word
                nodeNums += 1

        # 连接单词以及变换的词之间的边
        def addEdge(word):
            numberingWord(word)

            srcNodeID = nodes[word]

            chars = list(word)

            for i in range(len(chars)):
                # 对词中的每一个字符进行变换
                tmp = chars[i]
                chars[i] = '*'
                newWord = "".join(chars)
                numberingWord(newWord)
                dstNodeID = nodes[newWord]

                # 无向图
                # 变换后的新词与原词两个节点用边相连
                edge[srcNodeID].append(dstNodeID)
                edge[dstNodeID].append(srcNodeID)

                chars[i] = tmp

        nodeNums = 0
        
        # 对词典中的词进行建图
        for word in wordList:
            addEdge(word)

        # 对起始单词进行建图
        addEdge(beginWord)
        beginID = nodes[beginWord]

        # 如果终止单词不再图中则直接返回0
        if endWord not in nodes:
            return 0

        endID = nodes[endWord]
        edge = collections.defaultdict(list)
        queue = collections.deque([beginID])
        dist = [float("inf")] * nodeNums

        # BFS
        while queue:
            x = queue.popleft()
            if x == endWord:
                return dist[endID] // 2 + 1
            
            for it in edge[x]:
                if dist[it] == float("inf"):
                    dist[it] = dist[x] + 1
                    queue.append(it)
        return 0

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target not in nums:
            return [-1, -1]

        if len(nums) == 1:
            return [0, 0]

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                left = mid
                right = mid
                while left - 1 >= low and nums[left] == nums[left - 1]:
                    left -= 1
                while right + 1 <= high and nums[right] == nums[right + 1]:
                    right += 1

                return [left, right]

            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        n = len(s)
        ret = 0
        index = 0
        
        for i in range(n):
            if index < len(g) and g[index] <= s[i]:
                ret += 1
                index += 1

        return ret

    def maxProfit(self, prices: List[int]) -> int:
        dp = [ [0] * 2 for _ in range(len(prices)) ]
        print(len(dp))
        n = len(prices)
        
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            print(i)
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[n - 1][0]

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        direction = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, 1), (1, -1), (-1, -1), (1, 1)]

        def countMiners(x, y):
            """
            docstring
            """
            cnt = 0

            for dir_x, dir_y in direction:
                tx = x + dir_x
                ty = y + dir_y

                if not(0 < tx <= len(board) and 0 < ty <= len(board[0])):
                    continue

                cnt += board[tx][ty] == 'M'

            return cnt

        def dfs(x, y):
            cnt = countMiners(x, y)

            if cnt > 0:
                board[x][y] = str(cnt)  
            else:
                board[x][y] = 'B'
                for dir_x, dir_y in direction:
                    tx = x + dir_x
                    ty = y + dir_y
                    if not(0 < tx <= len(board) and 0 < ty <= len(board[0])) or board[tx][ty] != 'E':
                        continue
                    dfs(tx, ty)

        x = click[0]
        y = click[1]

        if (board[x][y] == 'M'):
            board[x][y] = 'X'
        else:
            dfs(x, y)

        return board

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        tmp = []
        def backtrack(index):
            if index == len(nums):
                ret.append(tmp.copy())
                return

            tmp.append(nums[index])
            backtrack(index + 1)
            tmp.pop()
            backtrack(index + 1)

        backtrack(0)

        return ret

    def combine(self, n: int, k: int) -> List[List[int]]:
        tmp = []
        ret = []

        def backtrack(index):
            if len(tmp) + (n - index + 1) < k:
                return 

            if len(tmp) == k:
                ret.append(tmp.copy())
                return

            tmp.append(index)
            backtrack(index + 1)
            tmp.pop()
            backtrack(index + 1)

        backtrack(1)

        return ret

    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        
        def backtrack(index):
            if index == len(nums):
                ret.append(nums.copy())

            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                backtrack(index + 1)
                nums[i], nums[index] = nums[index], nums[i]

        backtrack(0)
        
        return ret

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm = []
        ret = []
        visited = [0] * len(nums)

        def backtrack(index):
            if index == len(nums):
                ret.append(perm.copy())
                return 

            for i in range(len(nums)):
                if visited[i] != 0 or (i > 0 and nums[i - 1] == nums[i] and visited[i - 1] == 0):
                    continue

                perm.append(nums[i])
                visited[i] = 1
                backtrack(index + 1)
                visited[i] = 0
                perm.pop()

        sorted(nums)
        
        backtrack(0)

        return ret

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combine = []
        combines = []

        def backtrack(target, index):
            if index == len(candidates):
                return
            
            if target == 0:
                combines.append(combine.copy())
                return

            backtrack(target, index + 1)

            if target - candidates[index] >= 0:
                combine.append(candidates[index])
                backtrack(target - candidates[index], index)
                combine.pop()

        backtrack(target, 0)

        return combines
        


class Test(unittest.TestCase):
    def testSearchRange(self):
        """
        docstring
        """
        self.assertEqual(Solution().searchRange([1, 4], 4), [1, 1])
        
    def testFindContentChildren(self):
        """
        docstring
        """
        self.assertEqual(Solution().findContentChildren([10,9,8,7], [5, 6, 7, 8]), 2)

    def testMaxProfit(self):
        self.assertEqual(Solution().maxProfit([7,1,5,3,6,4]), 7)

    def testUpdateBoard(self):
        self.assertEqual(Solution().updateBoard([['E', 'E', 'E', 'E', 'E'], \
                                                 ['E', 'E', 'M', 'E', 'E'], \
                                                 ['E', 'E', 'E', 'E', 'E'], \
                                                 ['E', 'E', 'E', 'E', 'E']], [3, 0]), 
                                                 [['B', '1', 'E', '1', 'B'], \
                                                 ['B', '1', 'M', '1', 'B'],  \
                                                 ['B', '1', '1', '1', 'B'],  \
                                                 ['B', 'B', 'B', 'B', 'B']])

    def testSubSets(self):
        """
        
        """
        self.assertEqual(Solution().subsets([1, 2, 3]), [[1,2,3],[1,2],[1,3],[1],[2,3],[2],[3],[]])

    def testCombine(self):
        """
        
        """
        self.assertEqual(Solution().combine(4, 2), [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]])

    def testPermute(self):
        """
        
        """
        self.assertEqual(Solution().permute([1, 2, 3]), [
                                                        [1,2,3],
                                                        [1,3,2],
                                                        [2,1,3],
                                                        [2,3,1],
                                                        [3,1,2],
                                                        [3,2,1]
                                                        ])

    def testPermuteUnique(self):
        """
        
        """
        self.assertEqual(Solution().permuteUnique([1, 1, 2]), [[1,1,2],[1,2,1],[2,1,1]])

if __name__ == "__main__":
    unittest.main()
