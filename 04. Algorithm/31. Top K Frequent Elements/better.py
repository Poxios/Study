## better than books!

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return next(zip(*Counter(nums).most_common(k))