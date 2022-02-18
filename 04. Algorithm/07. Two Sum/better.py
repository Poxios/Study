# 1. using 'in' keyword instead of compare on python
# 2. instead find value in array, using dictionary's key - matching function
# 3. instead using two for, combine them into a single for - saving spaces too

# https://leetcode.com/problems/two-sum/
from typing import Dict, List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      nums_map = {}
      for i, num in enumerate(nums):
        nums_map[num] = i
        
      for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
          return [i, nums_map[target - num]]
