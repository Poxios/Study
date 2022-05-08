from functools import total_ordering
from typing import Dict, List

# get min height, erase them in order

class Solution:
  def trap(self, height: List[int]) -> int:
    # Cut longest line to second one
    maxHeight = max(height)
    if height.count(maxHeight) == 1 and len(height) != 1:
      height[height.index(maxHeight)] = max([x for x in height if x != maxHeight])
    
    total_hole_count = 0
    while True:
      # print(height)
      if height.count(height[0]) == len(height):
        break
      minHeight = min(height)
      for i, h in enumerate(height):
        if minHeight == h:
          # print('found '+str(i))
          height[i]+=1
          left, right = i-1 , i+1
          hole_count = 1
          can_trap=True
          # 1. Left
          while True:
            # Case 0. End of space, cannot be trapped
            if left == -1:
              can_trap = False
              break
            # Case 1. Blocked by wall
            if height[left] > minHeight:
              break
            # Case 2. Same height, keep going
            elif height[left] == minHeight:
              height[left] += 1
              left -= 1
              hole_count += 1

          # 2. Right
          while True:
            # Case 0. End of space, cannot be trapped
            if right == len(height):
              can_trap = False
              break
            # Case 1. Blocked by wall
            elif height[right] > minHeight:
              break
            # Case 2. Same height, keep going
            elif height[right] == minHeight:
              height[right] += 1
              right += 1
              hole_count += 1
          # If it can be trapped, plus to total count
          if can_trap:
            total_hole_count += hole_count
    return total_hole_count