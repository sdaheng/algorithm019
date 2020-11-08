import unittest

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def createLinkedList(list):
    """
    
    """

    head = ListNode(0)
    cur = head

    for item in list:
        node = ListNode(item)
        cur.next = node
        cur = node

    return head.next
    
def linkedList2List(head):
    """
    
    """
    ret = []
    cur = head
    while cur:
        ret.append(cur.val)
        cur = cur.next

    return ret
        


class Practice:
    def maxArea(self, height):
        if not height:
            return 0

        left = 0
        right = len(height) - 1

        area = 0
        while left < right:
            area = max(area, min(height[left], height[right]) * (right - left))

            if height[right] > height[left]:
                left += 1
            else:
                right -= 1

        return area
    
    def twoSum(self, nums, target):

        if not nums:
            return []

        hashTable = {}
        
        for i, num in enumerate(nums):
            if target - num in hashTable:
                return [hashTable[target - num], i]
            hashTable[num] = i

        return []

    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        cur = 0

        for num in nums:
            if num != 0:
                nums[cur] = num
                cur += 1

        for i in range(cur, len(nums)):
            nums[i] = 0

    def climbStairsWithDPArray(self, n):
        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
    
    def climbStairsWithoutDPArray(self, n):
        p = 0
        q = 0
        r = 1
        
        for _ in range(1, n + 1):
            p = q
            q = r
            r = p + q

        return r

    def threeSum(self, nums):
        if not nums:
            return []

        n = len(nums)
        if n < 3:
            return []

        nums.sort()
        result = []

        for i in range(n):
            if nums[i] > 0:
                return result

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                summ = nums[i] + nums[left] + nums[right]

                if summ == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif summ < 0:
                    left += 1
                else:
                    right -= 1

        return result
    
    def reverseList(self, head):
        newHead = ListNode(0)
        cur = head
        while cur:
            node = ListNode(cur.val)
            node.next = newHead.next
            newHead.next = node
            cur = cur.next

        return newHead.next

    def swapPairs(self, head):
        if not head or not head.next:
            return head
        
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head

        return newHead

    def reverseKGroup(self, head, k):
        def reverse(self, head, tail):
            prev = tail.next
            p = head
            while prev != tail:
                nex = p.next
                p.next = prev
                prev = p
                p = nex
            return tail, head

        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next
        
        return hair.next


class Test(unittest.TestCase):
    """
    
    """
    def testMaxArea(self):
        self.assertEqual(Practice().maxArea([1,8,6,2,5,4,8,3,7]), 49)
    
    def testTwoSum(self):
        """
        
        """
        self.assertEqual(Practice().twoSum([2, 7, 11, 15], 9), [0, 1])

    def testMoveZeros(self):
        nums = [0,1,0,3,12]
        Practice().moveZeroes(nums)
        self.assertEqual(nums, [1,3,12,0,0])

    def testClimbStairsWithDPArray(self):
        self.assertEqual(Practice().climbStairsWithDPArray(2), 2)

    def testClimbStairsWithoutDPArray(self):
        self.assertEqual(Practice().climbStairsWithoutDPArray(2), 2)

    def testThreeSum(self):
        """
        
        """
        self.assertEqual(Practice().threeSum([-1, 0, 1, 2, -1, -4]).sort(), [[-1, 0, 1], [-1, -1, 2]].sort())
        self.assertEqual(Practice().threeSum([0, 0, 0, 0]).sort(), [[0, 0, 0, 0]].sort())

    def testReverseList(self):
        """
        
        """
        self.assertEqual(linkedList2List(Practice().reverseList(createLinkedList([1, 2, 3, 4, 5]))), [5, 4, 3, 2, 1])
    
    def testSwapPairs(self):
        """
        
        """
        self.assertEqual(linkedList2List(Practice().swapPairs(createLinkedList([1, 2, 3, 4]))), [2, 1, 4, 3])

    def testTrap(self):
        self.assertEqual(HomeworkWeek1().trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)
if __name__ == "__main__":
    unittest.main()