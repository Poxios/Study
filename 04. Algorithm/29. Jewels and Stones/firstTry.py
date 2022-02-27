# jewels = "aA", stones = "aAAbbbb"

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_type = [x for x in jewels]
        count = 0
        for c in stones:
            if c in jewels_type:
                count += 1
        return count