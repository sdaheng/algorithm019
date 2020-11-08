import unittest

class HomeworkWeek1:
    def trap(self, height):
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        ans = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += (left_max - height[left])

                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += (right_max - height[right])
                right -= 1
        return ans

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.deque = [0] * (k + 1)
        self.size = 0
        self.cap = k + 1
        self.front = 0
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            self.front = (self.front - 1 + self.cap) % self.cap
            self.deque[self.front] = value
            return True
        return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            self.deque[self.rear] = value
            self.rear = (self.rear + 1) % self.cap
            return True
        return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.front = (self.front + 1) % self.cap
            return True
        return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.rear = (self.rear - 1 + self.cap) % self.cap
            return True
        return False
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if not self.isEmpty():
            return self.deque[self.front]
        return -1
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if not self.isEmpty():
            return self.deque[(self.rear - 1 + self.cap) % self.cap]
        return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.front == self.rear

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return (self.rear + 1) % self.cap == self.front

class Test(unittest.TestCase):
    def testTrap(self):
        self.assertEqual(HomeworkWeek1().trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)

    def testCircularDeque(self):
        """
        ["MyCircularDeque","insertLast","insertLast","insertFront","insertFront","getRear","isFull","deleteLast","insertFront","getFront"]
        [[3],[1],[2],[3],[4],[],[],[],[4],[]]
        """
        obj = MyCircularDeque(3)
        param_1 = obj.insertLast(1)
        self.assertTrue(param_1)
        param_2 = obj.insertLast(2)
        self.assertTrue(param_2)
        param_3 = obj.insertFront(3)
        self.assertTrue(param_3)
        param_4 = obj.insertFront(4)
        self.assertFalse(param_4)
        param_5 = obj.getRear()
        self.assertEqual(param_5, 2)
        param_6 = obj.isFull()
        self.assertTrue(param_6)
        param_7 = obj.deleteLast()
        self.assertTrue(param_7)
        param_8 = obj.insertFront(4)
        self.assertTrue(param_8)
        param_9 = obj.getFront()
        self.assertEqual(param_9, 4)

if __name__ == "__main__":
    unittest.main()
