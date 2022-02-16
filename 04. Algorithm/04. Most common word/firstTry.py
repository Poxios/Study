import re
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        purified_word = re.sub('[^a-zA-Z ]+',' ', paragraph)

        paragraph_word_list = purified_word.split()
        counter = {}
        for word in paragraph_word_list:
            lw = word.lower()
            if lw in counter:
                counter[lw]+=1
            else:
                counter[lw]=1
        counter_sorted = sorted(counter.items(), key=lambda x: x[1],reverse=True)
        print(counter_sorted)
        for count in counter_sorted:
            if count[0] not in banned:
                return count[0]