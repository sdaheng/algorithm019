package main

func twoSum(nums []int, target int) []int {
	// 1. hash
	// 每次从hash表中查询target-n的元素是否在hash表中
	// 如果在则返回索引
	// 否则向hash表中存储当前元素索引
	mmap := map[int]int{}
	for i, n := range nums {
		if p, ok := mmap[target - n]; ok {
			return []{p, i}
		}
		mmap[target - n] = i
	}
	return nil
}

func isAnagram(s string, t string) bool {
	// hash表
	// 思路：
	// 对两个字符串进行遍历，在遍历其中一个字符串的时候在hash表中统计字母出现个数
	// 在对另一个字符串遍历时减少相同字母个数
	// 如果hash表中全部字母对统计个数为0则是异位词，否则不是

	if len(s) != len(t) {
		return false
	}

	table := make([]int, 26)

	for _, c := range s {
		table[c - 'a']++
	}

	for _, c:= range t {
		table[c - 'a']--
	}

	for _, n := range table {
		if n != 0 {
			return false
		}
	}

	return true
}

func preorder(root *Node) (result []int) {
   if root == nil {
		return nil
	}

	recursive = func (root *Node) {
		if root == nil {
			return
		}
	
		result = append(result, root.Val)
	
		for _, child := range root.Children {
			recursive(child, ret)
		}
	}
	recursive(root)

	return 
}

func inorderTraversal(root *TreeNode) (result []int) {
    if root == nil {
        return nil
    }

    var recursive func (root *TreeNode)

    recursive = func (root *TreeNode) {
        if root == nil {
            return
        }
        recursive(root.Left)
        result = append(result, root.Val)
        recursive(root.Right)
    }

    recursive(root)

    return
}

func preorderTraversal(root *TreeNode) (result []int) {
    if root == nil {
        return nil
    }

    var recursive func (root *TreeNode)

    recursive = func (root *TreeNode) {
        if root == nil {
            return
        }
        result = append(result, root.Val)
        recursive(root.Left)
        recursive(root.Right)
    }

    recursive(root)

    return
}

func min(list []int) int {
    if len(list) == 0 {
        return 0
    }
    s = sort(list)
    return s[0]
}

func nthUglyNumber(n int) int {
    dp := make([]int, n)
    a := 0
    b := 0
    c := 0

    for i = 1; i < n; i++ {
        n2, n3, n5 = dp[i] * 2, dp[i] * 3, dp[i] * 5
        dp[i] = min([]int{n2, n3, n5})
        if dp[i] == n2 {
            a++
        }

        if dp[i] == n3 {
            b++
        }

        if dp[i] == n5 {
            c++
        }
    }

    return dp[len(dp) - 1]
}

func numIslands(grid [][]byte) int {
    m := len(grid)
    n := 0
    if m > 0 {
        n = len(grid[0])
    }

    var dfsFunc func (x, y int)

    ans := 0
    dfsFunc = func(x, y int) {
        if !((x >= 0 && x < m) || (y >= 0 && y < n)) {
            return
        }

        grid[x][y] = 2

        directions := [][]int{[]int{x + 1, y}, []int{x - 1, y}, []int{x, y + 1}, []int{x, y - 1}}

        for _, direction := range directions {
            r, c := direction[0], direction[1]
            if r >= 0 && r < m && c >= 0 && c < n && grid[r][c] == '1' {
                dfsFunc(direction[0], direction[1])
            }
        } 
    }

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == '1' {
                dfsFunc(i, j)
                ans++
            }
        }
    }

    return ans
}

func permute(nums []int) [][]int {
    if len(nums) == 0 {
        return nil
    }

    n := len(nums)

    ret := [][]int{}

    var backtrack func (p int)

    backtrack = func (p int) {
        if p == n {
            ret = append(ret, nums)
        }

        for i := p; i < n; i++ {
            nums[i], nums[p] = nums[p], nums[i]
            backtrack(p + 1)
            nums[i], nums[p] = nums[p], nums[i]
        }
    }

    backtrack(0)

    return ret
}

func main() {
    permute([]int{1, 2 ,3})
}
