class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols =len(image), len(image[0])
        org= image[sr][sc]
        def dfs(r, c):
            if r<0 or r>=rows or c<0 or c>=cols or image[r][c]== color:
                return
            elif image[r][c] == org:
                image[r][c] = color
                dfs(r-1, c)
                dfs(r+1, c)
                dfs(r, c-1)
                dfs(r, c+1)
            else:
                return

            

        dfs(sr, sc)

        return image