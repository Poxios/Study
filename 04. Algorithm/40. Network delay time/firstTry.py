# [[2,1,1],[2,3,1],[3,4,1]]

import collections
from heapq import heappop, heappush


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist_map = collections.defaultdict(list)
        for depart, arrive, dist in times:
            dist_map[depart].append((arrive, dist))
        min_queue = [(0, k)]
        dist_result = {}
        while min_queue:
            time, arrived_at = heappop(min_queue)
            if arrived_at not in dist_result:
                dist_result[arrived_at] = time
                for arrive, dist in dist_map[arrived_at]:
                    alt = time + dist
                    heappush(min_queue, (alt, arrive)) # need to know - add value without finding min value
        if len(dist_result) == n:
            return max(dist_result.values())
        return -1