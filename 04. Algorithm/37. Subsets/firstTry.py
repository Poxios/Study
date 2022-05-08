import enum
import itertools
from typing import List

# 1,2,3


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def dfs(candidates: list, basket: list):
            results.append(basket)
            
            for idx, num in enumerate(candidates):
                dfs(candidates[idx + 1:], basket + [num])

        dfs(nums, [])
        return results

s=Solution()
s.subsets([1,2,3])