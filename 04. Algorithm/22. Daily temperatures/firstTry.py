# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tDict = [0 for _ in temperatures]

        stack = []
        for idx, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                idx_before = stack.pop()[0]
                tDict[idx_before] += idx - idx_before
            stack.append((idx, t))

        return tDict
