# 笔记

- [笔记](#笔记)
  - [数据结构](#数据结构)
    - [线性表](#线性表)
    - [数组](#数组)
    - [链表](#链表)
    - [跳表](#跳表)
    - [栈](#栈)
    - [队列](#队列)
    - [哈希表](#哈希表)
    - [映射](#映射)
    - [集合](#集合)
    - [树](#树)
    - [堆](#堆)
    - [图](#图)
  - [算法思想](#算法思想)
    - [回溯](#回溯)
    - [分治](#分治)
    - [贪心](#贪心)
    - [动态规划](#动态规划)
  - [搜索算法](#搜索算法)
    - [DFS](#dfs)
    - [BFS](#bfs)
    - [Binary Search](#binary-search)

## 数据结构
### 线性表

线性表是n个数据元素的有限序列，相邻数据元素之间存在着序偶关系
                                      
### 数组
线性结构
存储方式为连续存储
通过随机访问的方式以O(1)的时间复杂度获取数组中的元素。

**增加元素**
在尾部增加元素时间复杂度为O(1)
其他部分需要向后挪动元素，时间复杂度为O(n)

**删除元素**
在尾部删除元素时间复杂度为O(1)
其他部分需要向后挪动元素，时间复杂度为O(n)

**题型**
1. 双指针
2. 滑动窗口
3. 搜索

### 链表
线性结构
存储方式为非连续存储
类型分为单链表，双链表，循环链表
单链表通过next指针向后遍历，双链表比单链表多了previous指针指向前一个节点。循环链表比前述两种链表在链表尾部重新指向头节点
获取元素的时间复杂度为O(n)

**增加元素**
将新节点的next指针指向待插入位置的后一个节点，将待插入位置的原节点指向新节点

**删除元素**

**题型**
1. 逆序链表
2. 判断环形链表
3. 合并链表

### 跳表
只能用于元素有序的情况

### 栈

**题型**
1. 括号匹配
2. 最小栈
3. 用队列实现栈

### 队列

### 哈希表

**题型**


### 映射

### 集合

### 树

**题型**
1. 遍历 二叉树，多叉树的前中后层序遍历
2. 翻转
3. 验证二叉排序树
4. 建立二叉树
5. 求树的最大，最小深度
6. 公共祖先

**模版**

递归前序遍历二叉树
```
def preorder_recursive_traverse(root):
    if not root:
        return None

    process(root) # 处理节点

    preorder_recursive_traverse(root.left)
    preorder_recursive_traverse(root.right)

``` 

递归中序遍历二叉树
```
def inorder_recursive_traverse(root):
    if not root:
        return None

    inorder_recursive_traverse(root.left)

    process(root) # 处理节点

    inorder_recursive_traverse(root.right)

``` 

递归后序遍历二叉树
```
def backorder_recursive_traverse(root):
    if not root:
        return None

    backorder_recursive_traverse(root.left)

    process(root) # 处理节点

    backorder_recursive_traverse(root.right)

``` 

二叉树层序遍历
```
def levelorder_traverse(root):
    if not root:
        return None

    queue = [root]
    while queue:
        queue_size = len(queue)
        for i in range(queue_size):
            node = queue.pop(0) # 获取队头元素
            
            # process node

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


```
### 堆
可以迅速找到一堆数中的最大或最小值的一种数据结构

根节点为所有数中最大值的对叫大根堆，最小值的为小根堆

堆的类型：
1. 二叉堆
2. 斐波那契堆

**二叉堆**
二叉堆是一颗完全二叉树
树中任意节点的值都大于等于它子节点的值

实现：
一般通过数组的方式存储二叉堆
当根节点索引为0时，如果父节点索引为i，则左孩子索引为$(2 * i + 1)$，右孩子节点索引为$(2 * i + 2)$，父节点索引为$floor((i - 1) / 2)$

**操作**
1. 插入
   将节点插入到尾部，然后向上调整
2. 删除
   将堆顶与堆尾元素交换，然后向下调整


**题型**
1. K个最大，最小的数


### 图

**题型**
1. DFS
2. BFS
3. 最短路径


## 算法思想

### 回溯


**题型**
1. 括号生成
2. 排列组合
    1. 排列问题，要求数字之间的顺序，可使用visited数组标记已使用过的数字
    2. 组合问题，不要求数字之间的顺序，可使用index变量按顺序搜索（组合）数字

**剪枝**


### 分治

分治的基本思想是分而治之
分解->解决->合并
1. 将原问题分解为结构相同的子问题
2. 分解到某个容易求解的边界，递归求解
3. 把子问题的解合并成原问题的解

问题可以分解成为最优子结构
各个子问题相互独立

**模版**

```
def divide_conquer(problem, para1, para2, ...):
    if proble is None:
        # return results
        return 
    
    data = generate_data(problem)
    subproblems = split_problem(problem, data)

    sub_result1 = divide_conquer(subproblems[0], para1, para2, ...)
    sub_result2 = divide_conquer(subproblems[1], para1, para2, ...)
    ...

    results = process_result(sub_result1, sub_result2, ...)
```

**题型**
1. 归并
2. 最小k个数
3. 快排

### 贪心

每一步仅考虑当前的最优结果，适用于具有最优子结构的问题

**证明方法**
1. 反证法
2. 递推法

**排序解法**
**反悔解法**

与动态规划的区别：
动态规划根据之前的结果对当前进行选择

**题型**
1. 找零

### 动态规划
最优子结构

存最优的解

## 搜索算法

### DFS

**模版**
```
def dfs_recursive(node, visited):
    # Terminate condition
    if node in visited:
        return # 不重复访问

    visited.append(node)

    # process current node

    for child in node.children:
        if child not in visited:
            dfs_recursive(child, visited)    
```

### BFS

**模版**

```
def bfs(node, visited):
    queue = [node]
    while queue:
        queu_size = len(queue)
        for i in range(queue_size):
            nodee = queue.pop()
            visited.append(nodee)

            # process node

            for child in nodee.related_nodes():
                if child not in visited:
                    queue.append(child)
    
```

### Binary Search

**模版**

```
def binary_search(nums, target):
    # nums is sorted

    low = 0
    high = len(nums) - 1

    while left <= high:
        mid = left + (right - left) / 2

        if nums[mid] == target:
            # process result
            return result
        elfi nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1     
```

