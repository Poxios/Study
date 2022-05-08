from typing import Dict, List

# need to know - product is magic..


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        for i in range(0, len(nums)):
            out.append(p)
            p = p*nums[i]
        # list of left products is waiting for right product list
        p = 1
        for i in range(len(nums)-1, -1, -1):
            out[i] = out[i]*p
            p = p*nums[i]
        return out
