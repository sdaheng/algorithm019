学习笔记

### LRU Cache

Hash table + 双向链表

通过哈希表查询是否存在于cache中，最久未使用的放在链表尾。

### 布隆过滤器

布隆过滤器是一个通过长二进制数组及哈希函数来判断元素是否在一个集合中

**原理**

将元素通过k个哈希函数，得到在长二进制数组中的k个位置，并将所有位置的值置为1

在检索时，如果经过k个哈希函数得到当k个位置上的值都为1则表示集合中存在这个元素
当k个位置上有一个不为1，则集合中不存在此元素。

![布隆过滤器](./Bloom.png)

**优点**

空间效率和查询效率高

**缺点**

有一定的误判率且删除困难

### 排序

**冒泡排序**

```
def bubbleSort(num):
    if not num:
        return num
    for i in range(len(num)):
        for j in range(len(num) - 1 - i):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    return num
```

**选择排序**

```
def selectionSort(num):
    if not num:
        return num

    minIndex = 0

    for i in range(len(num)):
        minIndex = i

        for j in range(i + 1, len(num)):
            if num[j] < num[minIndex]:
                minIndex = j

        num[i], num[minIndex] = num[minIndex], min[i]
    
    return num
```


