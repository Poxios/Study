from typing import Dict, List

# using slicer is always great

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
      return sum(sorted(nums[::2]))