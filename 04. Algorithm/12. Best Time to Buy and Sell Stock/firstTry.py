from typing import Dict, List

# [3,2,6,5,0,3]
# [0,1,2,3,4,5]

# [0,2,3,3,5,6]
# [4,1,0,5,3,2]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p_dict = {}
        for i, p in enumerate(prices):
            p_dict[i] = p
        p_dict = sorted(p_dict.items(),key=lambda x:x[1])
        # return p_dict
        for indexA, valueA in p_dict:
          for indexB, valueB in p_dict[::-1]:
            if indexA == indexB:
              break
            if indexA < indexB:
              return valueB-valueA
        return 0





s= Solution()
print(s.maxProfit([7,1,5,3,6,4]))