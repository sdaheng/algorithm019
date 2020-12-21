from typing import List
import collections
import unittest

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [ [0] * len(grid[0]) for _ in range(len(grid)) ]
        dp[0][0] = grid[0][0]

        for i in range(1, len(grid[0])):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for j in range(1, len(grid)):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, len(grid[0])):
            for j in range(1, len(grid)):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[len(grid[0]) - 1][len(grid) - 1]

    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        dp = [1] * (len(s) + 1)

        for i in range(2, len(s) + 1):
            if s[i - 1] == '0' :
                if s[i - 2] == '1' or s[i - 2] == '2':
                    dp[i] = dp[i - 2]
                else:
                    return 0
            elif s[i - 2] == '1' or s[i - 2] == '2' and '1' <= s[i - 1] <= '6':
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]

        return dp[len(s)]
    
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        if not matrix[0]:
            return 0

        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        result = 0

        for i in range(len(matrix[0])):
            dp[i][0] = int(matrix[i][0])
            result = max(dp[i][0], result)

        for j in range(len(matrix)):
            dp[0][j] = int(matrix[0][j])
            result = max(dp[0][j], result)

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    result = max(dp[i][j], result)
        
        return result * result

    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 任务次数
        freq = collections.Counter(tasks)

        # 任务执行最多的次数
        maxExec = max(freq.values())

        # 统计执行最多次数的任务个数
        maxCount = sum(1 for v in freq.values() if v == maxExec)

        # 返回存在冷却时间的任务执行之间与不存在冷却时间的任务执行时间的最大值
        return max((maxExec - 1) * (n + 1) + maxCount, len(tasks))

    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        counts = 0

        for i in range(len(s)):
            for j in range(i):
                if i == j:
                    dp[i][j] = True
                    counts += 1
                elif j - i == 1 and s[i] == s[j]:
                    dp[i][j] = True
                    counts += 1
                elif j - i > 1 and s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    counts += 1
        return counts

    # dp[i][j - 1]表示word1新增一个字符
    # dp[i - 1][j]表示word1删除一个字符 
    # dp[i - 1][j - 1]表示用word2最后一个字符替换了word1最后一个字符，替换后可以一起删除
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        if n * m == 0:
            return n + m

        dp = [[0] * (m + 1) for _ in range((n + 1))]

        for i in range(n + 1):
            dp[i][0] = i

        for j in range(m + 1):
            dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = dp[i - 1][j] + 1
                down = dp[i][j - 1] + 1
                leftDown = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    leftDown += 1
                dp[i][j] = min(left, down, leftDown)

        return dp[n][m]

   def fib_recursive(self, n):
        """
        
        """
        if n == 1 or n == 2:
            return 1

        return self.fib_recursive(n - 1) + self.fib_recursive(n - 2)

    def fib_memo(self, n):
        memo = [0] * (n + 1)

        def _fib_memo(N):
            """
            docstring
            """
            if N == 1 or N == 2:
                return 1

            if memo[N] != 0:
                return memo[N]

            memo[N] = _fib_memo(N - 1) + _fib_memo(N - 2)  

            return memo[N]

        return _fib_memo(n)

class Test(unittest.TestCase):
    def testNumDecoding(self):
        self.assertEqual(Solution().numDecodings("1201234"), 3)

    def testFibMemo(self):
        self.assertEqual(Solution().fib_memo(30), 832040)

    def testFibRecursive(self):
        """
        
        """
        self.assertEqual(Solution().fib_recursive(30), 832040) 

if __name__ == "__main__":
    unittest.main()
