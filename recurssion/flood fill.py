class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        c = image[sr][sc]
        return self.flood(image, sr, sc, color, c)
    
    def flood(self, image: List[List[int]], sr: int, sc: int, color: int, c: int):
        rows = len(image)
        cols = len(image[0])
        if sr < 0 or sc <0 or sr> rows-1 or sc > cols-1: return image
        if image[sr][sc] == color:
            return image
        if image[sr][sc] == c: 
            image[sr][sc] = color
            self.flood(image, sr-1, sc, color, c)
            self.flood(image, sr, sc-1, color, c)
            self.flood(image, sr+1, sc, color, c)
            self.flood(image, sr, sc+1, color, c)
        return image
        