from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(num_left: list, basket: list):
            if len(num_left) == 1:
                result.append(basket + num_left)
            else:
                for n in num_left:
                    dfs([x for x in num_left if x != n], basket + [n])
        result = []
        dfs(nums, [])
        return result
