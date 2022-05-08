from typing import List

# https://leetcode.com/problems/reorder-data-in-log-files/

# 1. Letter Logs - consist only lowercase
# 2. Digit logs - consist only digits


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # sort function in python has key feature by lambda function.
        # in this situation, key by lambda function can have double item.
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits
