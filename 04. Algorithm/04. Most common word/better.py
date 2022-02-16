import collections
import re
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Need to know - list comprehension
        # [x for x in [] if x != 0]

        words = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]
        # Need to know - collections.Counter -> auto count words
        counts = collections.Counter(words)

        return counts.most_common(1)[0][0]