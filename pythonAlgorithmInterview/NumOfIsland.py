grid1 = [
    [1,1,1,1,0]
    [1,1,0,1,0],
    [1,1,0,0,0],
    [0,0,0,0,0]
]

grid1 = [
    11110
    [1,1,0,1,0],
    [1,1,0,0,0],
    [0,0,0,0,0]
]

class Solution:
    grid: List[List[str]]

    def dfs(self, i: int, j: int):
        # 더 이상 땅이 아닌 경우 종료
        if i < 0 or i >= len(self.grid) or \
            j < 0 or j >= len(self.grid[0]) or \
            self.grid[i][j] != '1':
            return

        grid[i][j] = '0' # 방문했던 곳 표기, 백트래킹

        # 동서남북 탐색
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            if self.grid[i][j] == '1':
                self.dfs(i, j)
                # 모든 육지 탐색 후 카운트 1 증가
                count += 1
        return count




