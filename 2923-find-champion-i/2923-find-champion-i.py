class Solution:
    def findChampion(self, grid):
        n = len(grid)

        for i in range(n):
            champion = True

            for j in range(n):
                if i != j and grid[i][j] == 0:
                    champion = False
                    break

            if champion:
                return i