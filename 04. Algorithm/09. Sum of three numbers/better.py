from typing import Dict, List

# [-1,0,1,2,-1,-4]
# [-4,-1,-1,0,1,2]

# Defeat factor: on 3sum calculation, if first number is fixed, last two pair
# cannot be changed only a number


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums)-2):
            # need to know - skip because all possible scenario wads done
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return results