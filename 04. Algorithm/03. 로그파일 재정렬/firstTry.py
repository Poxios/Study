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
            log_list = log.split(' ')
            identifier = log_list.pop(0)
            real_log = ''.join(log_list)
            if real_log.isalpha():
                letterLogList.append(log)
            else:
                digitLogList.append(log)

        print ('--------------------1')
        print(letterLogList)
        print ('--------------------2')
        print(digitLogList)

        # 2. Sort letter logs vs digit logs
        def get_real_log(log: str) -> str:
            log_list = log.split(' ')
            identifier = log_list.pop(0)
            return ''.join(log_list)

        letterLogList=sorted(letterLogList, key=lambda x: get_real_log(x))
        return letterLogList + digitLogList
