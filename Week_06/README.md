学习笔记

### 动态规划

动态规划方法主要用于求解**最优化问题**，这类问题看你包含多个解，每个解都有一个值，在这些解中找出一个最优的解。在求解过程中通过求局部子问题最优解达到全局最优解。

**与贪心，分治的区别**

贪心与分治都是将问题归结为更小的相似子问题，通过求解子问题得到全局最优解。

其中贪心算法的当前选择看你要以来已经做出的选择，但不依赖待做出的选择以及子问题。贪心法是自顶向下一步一步做出贪心选择

分治算法中的各个子问题是独立的，一旦递归的求出各子问题的解，便可自底向上的将子问题的解合并成问题的解。

如果当前的选择依赖于子问题的解，贪心算法难以通过局部贪心策略达到全局最优。如果子问题不独立，分治算法会重复求解子问题。

**由上述贪心与分治的问题，提出了动态规划方法。动态规划方法允许子问题不独立，也允许其通过自身子问题的解做出选择。**

**动态规划的解决方法**：通过记忆化解决子问题重复计算问题

**最优子结构**

问题的最优解包含了子问题的最优解

**重叠子问题**

问题的递归算法会反复的计算相同的子问题解

**实现方式**

自顶向下：从规模较大的问题**递归**分解成小的问题

自底向上：从小的问题**递推**到规模较大的问题

动态规划通常以**迭代**的方式自底向上的对问题进行求解

**步骤**
1. 刻画最优解结构
2. 递归定义最优解的值
3. 按自底向上或自顶向下记忆化的方式计算最优解的值，并记录下求解的路径
4. 按照求解途径给出最优解的形成过程

**状态转移方程**

1. 确定base case
2. 确定**状态**，即原问题和子问题中的变量
3. 确定**选择**，导致状态产生变化的行为
4. 明确dp数组的定义，例如把状态作为dp数组的索引

**技巧**

状态压缩

**时间复杂度**

时间复杂度 = 状态总数 * 每个状态的决策数 * 每次状态转移的时间

**优化策略**

动态规划的优化策略可以从时间复杂度中的三个方面来优化
1. 状态总数
   1. 改变状态表示
   2. 选择适当的规划方向
2. 状态的决策数
   1. 利用最优决策的单调性
   2. 优化决策量
   3. 合理组织状态
   4. 细化状态转移
3. 状态转移时间
   1. 减少决策时间
   2. 减少计算递推式时间


