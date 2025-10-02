class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        queue= deque()

        def bfs(r,c):
            if r <0 or r>=rows or c<0 or c>=cols or grid[r][c] == '0':
                return
            grid[r][c]='0'
            queue.append((r,c))           

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    bfs(r,c)

                    while queue:
                        k, l = queue.popleft()
                        bfs(k-1, l)
                        bfs(k+1, l)
                        bfs(k, l-1)
                        bfs(k, l+1)
                    count+=1 
        
        return count
                