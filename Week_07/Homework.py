from typing import List
import unittest
import collections

class Trie:
    """
    docstring
    """
    def __init__(self) -> None:
        self.root = {}
        self.endWord = "#"

    def insert(self, word):
        """
        docstring
        """
        node = self.root
        for char in word:
            node = node.setdefault(char, {})

        node[self.endWord] = self.endWord

    def search(self, word):
        """
        
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]

        return self.endWord in node

    def startWith(self, prefix):
        """
        docstring
        """
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True

class TestTrie(unittest.TestCase):
    def testTrieSearch(self):
        """
        docstring
        """
        trie = Trie()
        trie.insert("Trieee")
        self.assertEqual(trie.search("Triee"), False)

    def testTrieStartWith(self):
        """
        docstring
        """
        trie = Trie()
        trie.insert("Trieee")
        self.assertEqual(trie.startWith("Tri"), True)

class DisjointSet:
    """
    
    """
    def __init__(self, capacity) -> None:
        self.array = [ i for i in range(capacity) ]

    def union(self, i, j):
        """
        docstring
        """
        
        p1 = self.parent(i)
        p2 = self.parent(j)

        self.array[p1] = p2

    def parent(self, i):
        """
        docstring
        """
        root = i
        while self.array[root] != root:
            root = self.array[root]

        while self.array[i] != i:
            x = i
            i = self.array[i]
            self.array[x] = root

        return root
    
    def connected(self, i, j):
        """
        docstring
        """
        p1 = self.parent(i)
        p2 = self.parent(j)
        return p1 == p2

class TestDisjointSet(unittest.TestCase):
    def testUnion(self):
        """
        
        """
        disjointSet = DisjointSet(5)

        disjointSet.union(2, 3)

        self.assertTrue(disjointSet.connected(2, 3))

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def solve(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == '.':
                        for k in range(1, 9):
                            ch = str(k)
                            if isValid(i, j, ch):
                                board[i][j] = ch

                                if solve(board):
                                    return True
                                else:
                                    board[i][j] = '.'
                        return False

            return True

        def isValid(row, col, ch):
            for i in range(9):
                if board[i][col] != '.' and board[i][col] == ch:
                    return False
                if board[row][i] != '.' and board[row][i] == ch:
                    return False
                
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] != '.' and board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == ch:
                    return False

            return True

        if not board or not board[0]:
            return
        
        solve(board)

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def numberingGene(gene):
            if gene not in geneID:
                nonlocal nodeNums
                geneID[gene] = nodeNums
                nodeNums += 1

        def addEdge(gene):
            numberingGene(gene)
            srcNode = geneID[gene]

            geneList = list(gene)

            for i in range(len(geneList)):
                tmp = geneList[i]

                geneList[i] = "*"

                newGene = "".join(geneList)
                numberingGene(newGene)

                destNode = geneID[newGene]

                edge[srcNode].append(destNode)
                edge[destNode].append(srcNode)

                geneList[i] = tmp

        geneID = {}
        nodeNums = 0
        edge = collections.defaultdict(list) 

        for gene in bank:
            addEdge(gene)

        addEdge(start)

        if end not in bank:
            return -1

        # addEdge(end)

        dists = [float('inf')] * nodeNums
        startID, endID = geneID[start], geneID[end]
        dists[startID] = 0
        queue = collections.deque([startID])

        while queue:
            x = queue.popleft()
            if x == endID:
                return dists[endID] // 2 

            for it in edge[x]:
                if dists[it] == float('inf'):
                    dists[it] = dists[x] + 1
                    queue.append(it)

        return -1

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = 0
        if m > 0:
            n = len(grid[0])

        def dfs(grid, r, c):
            grid[r][c] = 0

            for x, y in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                    dfs(grid, x, y)

        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ret += 1
                    dfs(grid, i, j);

        return ret

class TestSolution(unittest.TestCase):
    def testSolveSudoku(self):
        """
        
        """
        sudoku = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

        Solution().solveSudoku(sudoku)
        print(sudoku)

if __name__ == "__main__":
    unittest.main()