import collections
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
