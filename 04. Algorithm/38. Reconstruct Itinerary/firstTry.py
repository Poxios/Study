# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# ["JFK","ATL","JFK","SFO","ATL","SFO"]

import collections
from heapq import heappop, heappush
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        book = collections.defaultdict(list)
        for e in tickets:
            heappush(book[e[0]], e[1])
        path = []
        def dfs(departed_at: str):
            path.append(departed_at)
            if book[departed_at]:
                dfs(heappop(book[departed_at]))
        dfs('JFK')
        return path

s=Solution()
s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])