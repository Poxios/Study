import collections
from heapq import heappop, heappush
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flight_map = collections.defaultdict(list)
        for u, v, w in flights:
            flight_map[u].append((v,w))
        Q = [(0, src, -1)]
        
        while Q:
            time, src, count = heappop(Q)
            if src == dst:
                return time
            if not count == k:
                for dst_temp, dist in flight_map[src]:
                    alt = dist + time
                    heappush(Q, (alt, dst_temp, count + 1))
        return -1

s=Solution()
print(s.findCheapestPrice(
4,
[[0,1,1],[0,2,5],[1,2,1],[2,3,1]],
0,
3,
1
))