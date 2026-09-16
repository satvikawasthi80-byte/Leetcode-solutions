class Solution:
    def countCollisions(self, directions):
        directions = directions.lstrip('L').rstrip('R')
        return len(directions) - directions.count('S')