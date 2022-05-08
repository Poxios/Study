import collections
import re
from typing import Dict, List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # len is same, elements are same.
        groups: Dict[str, List[str]] = {}
        for word in strs:
            strLen = len(word)
            str_components = sorted(list(word))
            key_name = str(strLen)+(''.join(str_components))
            if key_name in groups:
                groups[key_name].append(word)
            else:
                groups[key_name] = [word]
        print(groups)
        return [x[1] for x in groups.items()]
