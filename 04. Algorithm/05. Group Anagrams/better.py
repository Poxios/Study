import collections
import re
from typing import Dict, List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Remember, use defaultdict is always faster than divide by 'if'
        anagrams = collections.defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())