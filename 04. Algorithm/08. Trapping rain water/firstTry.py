from typing import Dict, List

class Solution:
  def trap(self, height: List[int]) -> int:
    totalHoleSize = 0
    index = 0
    while True:
      if index >= len(height) - 1:
        break
      if height[index + 1] < height[index]:
        canBlock = False
        for h in height[index + 1:]:
          if h >= height[index]:
            canBlock = True
            break
        if canBlock:
          startHeight = height[index]
          index += 1
          while height[index] < startHeight:
            
            totalHoleSize += startHeight - height[index]
            if index >= len(height)-1:
              break
            else:
              index += 1
      index += 1
      
    return totalHoleSize

a = Solution()
print(a.trap(height=[0,1,0,2,1,0,1,3,2,1,2,1]))
