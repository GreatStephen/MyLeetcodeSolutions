class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc]==newColor: return image
        R = len(image)
        C = len(image[0])
        def DFS(image, r, c, oldColor, newColor):
            if not(0<=r<R and 0<=c<C and image[r][c]==oldColor): return
            image[r][c] = newColor
            [DFS(image, r+x, c+y, oldColor, newColor) for (x,y) in ((-1,0),(0,1),(1,0),(0,-1))]
        
        DFS(image, sr, sc, image[sr][sc], newColor)
        return image