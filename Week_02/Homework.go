package main

type IHeap [][2]int

// 实现Sort接口，Len(), Less(), Swap()
func (h IHeap) Len() int {
    return len(h)
}

func (h IHeap) Less(i, j int) bool {
    return h[i][1] < h[j][1]
}

func (h IHeap) Swap(i, j int) {
    h[i], h[j] = h[j], h[i]
}

func (h *IHeap) Push(x interface{}) {
    *h = append(*h, x.([2]int))
}

func (h *IHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n - 1]
    *h = old[0 : n - 1]

    return x
}

// 前K个高频元素
// 思路：构建一个大根堆存放出现次数，遍历前K个堆元素得到前K个高频元素
func topKFrequent(nums []int, k int) []int {
    occurences := map[int]int{}

    for _, n := range nums {
        occurences[n]++
    }

    h = &IHeap{}
    heap.Init(h)

    for key, value := range occurences {
        heap.Push(h, [2]int{key, value})

        if h.Len() > k {
            heap.Pop(h)
        }
    }

    ret := make([]int, k)

    for i := 0; i < k; i++ {
        ret[k - i - 1] = heap.Pop(h).([2]int)[0]
    }

    return ret
}

// N叉树的层序遍历
// 思路：
// 通过队列先进先出的特性，将当前跟节点的孩子加入到队列中
// 对队列中所有节点进行遍历，每次取出队头作为当前的遍历节点，则可对树的当前层进行遍历
func levelOrder(root *Node) [][]int {
    if root == nil {
        return nil
    }

    ret := [][]int{}

    queue := []*Node{}
    queue = append(queue, root)
    for len(queue) > 0 {
        size := len(queue)
        res := []int{}
        for size > 0 {
            node := queue[0]
            queue = queue[1:]
            res = append(res, node.Val)

            for _, child := range node.Children {
                queue = append(queue, child)
            }

            size--
        } 
        ret = append(ret, res)
    }

    return ret
}