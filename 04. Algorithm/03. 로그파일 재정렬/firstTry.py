from typing import List

# https://leetcode.com/problems/reorder-data-in-log-files/

# 1. Letter Logs - consist only lowercase
# 2. Digit logs - consist only digits

# Letter logs must come before digit logs
# 

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 1. Divide Letter logs vs digit logs
        letterLogList = []
        digitLogList = []
        for log in logs:
            identifier = log.split(' ').pop(0)
            real_log = ''.join(log)
            if real_log.isalpha():
                letterLogList.append(log)
            else:
                digitLogList.append(log)

            """ for single_log in real_log:
                if single_log.isalpha():
                    letterLogList.append(single_log)
                else:
                    digitLogList.append(single_log) """

        # 2.