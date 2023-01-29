#leetcode 200.Number of Islands
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            # 탐색하다가 주변이 더 이상 땅이 아니면 종료한다.
            if i < 0 or i >= len(grid) or \
                    j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != '1':
                return

            # 방문한 곳은 0으로 표기한다. (방문했으니 다시 방문하지 말라는 뜻, 바다와 동일)
            grid[i][j] = 0

            # 주변을 탐색한다.
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # 그리드가 빈 행렬이면 0을 반환한다.
        if not grid:
            return 0

        # 그리드를 줄 단위로 탐색한다.
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):  # 옆 칸으로 이동해서 위를 반복한다. 전체 그리드를 탐색한다.
                if grid[i][j] == '1':
                    # 방문한 칸이 1일 경우, 연결된 부분(상하좌우 붙은 1) 탐색을 시작한다. 이미 방문했으면(0이면) 패스한다.
                    dfs(i, j)
                    # 1이 연결된 곳은 전부다 탐색했으면, 섬의 개수를 추가한다.
                    count += 1
        return count


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

solution = Solution()
print(solution.numIslands(grid))
