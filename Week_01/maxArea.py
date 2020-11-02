import unittest

class Solution:
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

class Test(unittest.TestCase):
    """
    
    """
    def testMaxArea(self):
        self.assertEqual(Solution().maxArea([1,8,6,2,5,4,8,3,7]), 49)

if __name__ == "__main__":
    unittest.main()