from typing import Dict, List

# Two Pointer
# Need to know - two pointer can do many things than just a pointer


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        volume = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]
        # When semi-max pole detected, pull the pole of other side
        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            if left_max <= right_max:
              volume += left_max - height[left]
              left += 1
            else:
              volume += left_max -height[right]
              right -= 1
        return volume
