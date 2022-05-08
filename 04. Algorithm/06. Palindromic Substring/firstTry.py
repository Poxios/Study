# 'abcbe' -> 'bcb'
# https://leetcode.com/problems/longest-palindromic-substring/submissions/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        def check_is_out_of_index(x):
            return len(s) - 1 < x or x < 0
        palindromeList = []
        if len(s) == 1:
            return s
        for i in range(len(s)):
            # Case 1. Odd Palindrome
            str_temp_list = [s[i]]
            i_left = i
            i_right = i
            while True:
                i_left -= 1
                i_right += 1
                if not check_is_out_of_index(i_left) and not check_is_out_of_index(i_right) and s[i_left] == s[i_right]:
                    str_temp_list.insert(0, s[i_left])
                    str_temp_list.append(s[i_right])
                else:
                    break
            if len(str_temp_list) != 1:
                palindromeList.append(''.join(str_temp_list))

            # Case 2. Even Palindrome
            str_temp_list = []
            i_left = i
            i_right = i+1
            while True:
                if not check_is_out_of_index(i_left) and not check_is_out_of_index(i_right) and s[i_left] == s[i_right]:
                    str_temp_list.insert(0, s[i_left])
                    str_temp_list.append(s[i_right])
                else:
                    break
                i_left -= 1
                i_right += 1

            if len(str_temp_list) != 0:
                palindromeList.append(''.join(str_temp_list))
        if len(palindromeList) == 0:
            return s[0]
        return max(palindromeList, key=len)
