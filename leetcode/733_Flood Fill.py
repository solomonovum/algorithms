class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # exception handling
        # The length of image and image[0] will be in the range [1, 50]
        if (len(image) < 1 or len(image) > 50) or (len(image[0]) < 1 or len(image[0]) > 50):
            return image

        if self.checkBoundary(image, sr, sc) is False:
            return image

        # The value of each color in image[i][j] and newColor will be an integer in [0, 65535]
        if newColor < 0 or newColor > 65535:
            return image

        # set visit map
        self.visit_map = [[0 for i in range(len(image[0]))] for j in range(len(image))]

        # set origin value
        self.origin_value = image[sr][sc]

        # run flood fill
        self.doDfs(image, sr, sc, newColor)

        return image

    def checkBoundary(self, image: List[List[int]], sr: int, sc: int) -> bool:
        # The given starting pixel will satisfy 0 <= sr < image.length and 0 1<= sc < image[0].length
        if (sr < 0 or sr >= len(image)) or (sc < 0 or sc >= len(image[0])):
            return False

    def doDfs(self, image: List[List[int]], sr: int, sc: int, newColor: int):
        # exception handling
        if self.checkBoundary(image, sr, sc) is False:
            return

        # exit condition
        if self.visit_map[sr][sc] is 1 or image[sr][sc] is not self.origin_value:
            return

        # set visit map
        self.visit_map[sr][sc] = 1

        # coloring
        image[sr][sc] = newColor

        # fill left
        self.doDfs(image, sr, sc - 1, newColor)
        # fill right
        self.doDfs(image, sr, sc + 1, newColor)
        # fill up
        self.doDfs(image, sr - 1, sc, newColor)
        # fill down
        self.doDfs(image, sr + 1, sc, newColor)
        
        
