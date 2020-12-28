import collections
from typing import List

class Solution:
    def hammingWeight(self, n):
        """
        docstring
        """
        ret = 0

        while n != 0:

            ret += 1
            n &= n - 1

        return ret

    def isPowerOfTwo(self, n):
        """
        docstring
        """
        
        return n > 0 and (n & (n - 1)) == 0

    def reverseBits(self, n):
        """
        docstring
        """
        ret = 0
        power = 31

        while n != 0:
            ret += (n & 1) << power
            n >>= 1
            power -= 1

        return ret
    
    def isAnagram(self, s, t):
        """
        docstring
        """
        if len(s) != len(t):
            return False
        return s.sort() == t.sort()
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # 对区间左端点排序
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果merged中最后一个区间的右端点 < 区间的左端点，即没有重合 则直接添加到merged中
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 有重合的情况下，将merged中最后一个区间的右端点改为区间的右端点
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

class LRUCache:

    def __init__(self, capacity: int):
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1

        value = self.dic.pop(key)
        self.dic[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dic.popitem(last=False)
            
        self.dic[key] = value

    