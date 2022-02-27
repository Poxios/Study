# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

from typing import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        for i in range(len(s), 0, -1):
            for j in range(len(s) - i+1):
                substr = s[j:j + i]
                if len(substr) == len(Counter(substr)):
                    return len(substr)
        return 0


s = Solution()
print(s.lengthOfLongestSubstring('abcabcbb'))
