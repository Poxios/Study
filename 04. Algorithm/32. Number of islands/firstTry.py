from typing import List

# [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_num = 0
        stack = []
        discovered = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) in discovered:
                    continue
                if grid[i][j] == '1':
                    island_num += 1
                    stack.append((i,j))
                    while stack:
                        v = stack.pop()
                        if not v in discovered:
                            discovered.append(v)
                            for x in [(v[0]-1,v[1]),(v[0]+1,v[1]),(v[0],v[1]+1),(v[0],v[1]-1)]:
                                if x in discovered or not (len(grid)>x[0]>=0 and len(grid[0])>x[1]>=0):
                                    continue
                                if grid[x[0]][x[1]] == "1":
                                    stack.append(x)
                                else:
                                    discovered.append(x)
                else:
                    discovered.append((i, j))
        return island_num


s = Solution()
print(s.numIslands(grid = 
[["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]]
))