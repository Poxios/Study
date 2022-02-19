from typing import Dict, List

# https://leetcode.com/problems/trapping-rain-water/

class Solution:
  def trap(self, height: List[int]) -> int:
    totalHoleSize = 0
    index = 0
    height.remove(max(height))

    while True:
      if index >= len(height) - 1:
        break
      if height[index + 1] < height[index]:
        startHeight = height[index]
        print('Detected: '+ str(startHeight))
        index += 1
        while height[index] < startHeight:
          totalHoleSize += startHeight - height[index]
          if index == len(height) - 1:
            break
          else:
            index += 1
      else:
        index += 1
    return totalHoleSize
