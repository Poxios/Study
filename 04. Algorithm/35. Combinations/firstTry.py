from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def dfs(num_left:list, depth:int, list_num: list):
            if depth == k:
                for n in num_left:
                    result.append(list_num + [n])
            else:
                for n in num_left[:]:
                    num_left.remove(n)
                    dfs(num_left[:], depth + 1, list_num + [n])
        dfs([x+1 for x in range(n)], 1, [])
        return result

s=Solution()
s.combine(3,3)