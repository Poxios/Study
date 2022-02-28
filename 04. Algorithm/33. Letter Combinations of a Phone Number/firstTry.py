class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        arrs = [dic[x] for x in digits]
        result = []

        def dfs(depth: int, word_made: str, r):
            if depth != len(arrs) - 1:
                for c in arrs[depth]:
                    dfs(depth+1, word_made+c,r)
            else:
                r += [word_made + x for x in arrs[depth]]

        dfs(0,'',result)
        return result
