import heapq
from typing import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums).most_common(k)
        return [v[0] for v in counter]
