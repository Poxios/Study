class Solution:
    def longestPalindrome(self, s: str) -> int:

        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # why left +1, right, not left, right + 1? -> moved one more than normal
            return s[left + 1:right]

        # Need to know - exceptions
        if len(s) < 2 or s == s[::-1]:
            return s
        result = ''
        # save only the longest pan, instead of saving all of pans
        for i in range(len(s) - 1):
          result = max(result, expand(i, i+1), expand(i,i+2), key=len)
        return result