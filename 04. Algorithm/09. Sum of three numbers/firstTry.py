from typing import Dict, List

# [-1,0,1,2,-1,-4]
# [-4,-1,-1,0,1,2]

# Failed


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        if nums.count(nums[0]) == len(nums) and nums[0] == 0 and len(nums) > 2:
            return [[0,0,0]]
        if nums.count(nums[0]) == len(nums):
            return []
        answer_list = []
        nums = sorted(nums)
        for i, n in enumerate(nums):
            list_left = nums[i+1:]
            can_pass = True
            while can_pass:
                can_pass = False
                left, right = 0, len(list_left) - 1
                while left < right:
                    if list_left[left] + list_left[right] == -1 * n:
                        if not [n, list_left[left], list_left[right]] in answer_list:
                            answer_list.append([n, list_left[left], list_left[right]])
                        list_left.pop(left)
                        list_left.pop(right-1)
                        can_pass = True
                        break
                    elif list_left[left] + list_left[right] > -1 * n:
                        right -= 1
                    else:
                        left += 1
        return answer_list
