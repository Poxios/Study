from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(candidates_left:list, list_num: list):
            for idx, n in enumerate(candidates_left):
                if sum(list_num) + n > target:
                    return
                elif sum(list_num) + n == target:
                    result.append(list_num + [n])
                else:
                    dfs(candidates_left[idx:], list_num + [n])
        dfs(sorted(candidates),[])
        return result