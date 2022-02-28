# Need to know - in array DFS, instead of making 'discovered' list, change value on original
# value array to prevent visit

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_num = 0
        stack = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    island_num += 1
                    stack.append((i,j))
                    while stack:
                        v = stack.pop()
                        grid[v[0]][v[1]] = '0'
                        for x in [(v[0]-1,v[1]),(v[0]+1,v[1]),(v[0],v[1]+1),(v[0],v[1]-1)]:
                            if (len(grid)>x[0]>=0 and len(grid[0])>x[1]>=0) and grid[x[0]][x[1]] == "1":
                                stack.append(x)
        return island_num
