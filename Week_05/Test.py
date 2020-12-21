from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        
        nums.sort()
        n = len(nums)
        
        ret = []
        for i in range(n):

            if nums[i] > 0:
                return ret
            
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            for j in range(i+1, n):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue

                left = j + 1
                right = n - 1
                
                while left < right:
                    _sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if _sum == target: 
                        ret.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        while left < right and nums[left + 1] == nums[left]:
                            left += 1

                        while left < right and nums[right - 1] == nums[right]:
                            right -= 1

                        left += 1
                        right -= 1
                    elif _sum < 0:
                        left += 1
                    else:
                        right -= 1
                        
        return ret

    def canJump(self, nums):
        """
        docstring
        """
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step
        
if __name__ == "__main__":
    # print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
    print(Solution().canJump([2,3,1,1,4]))
