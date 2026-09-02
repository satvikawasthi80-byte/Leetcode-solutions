class Solution:
    def maxArea(self, coords):
        def solve(points):
            min_x = float('inf')
            max_x = float('-inf')
            
            min_y = {}
            max_y = {}
            
            for x, y in points:
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                
                if x not in min_y:
                    min_y[x] = y
                    max_y[x] = y
                else:
                    min_y[x] = min(min_y[x], y)
                    max_y[x] = max(max_y[x], y)
            
            ans = 0
            
            for x in min_y:
                base = max_y[x] - min_y[x]
                height = max(x - min_x, max_x - x)
                
                ans = max(ans, base * height)
            
            return ans
        
        ans = solve(coords)
        
        # Swap x and y to check horizontal sides
        swapped = [(y, x) for x, y in coords]
        ans = max(ans, solve(swapped))
        
        return ans if ans > 0 else -1