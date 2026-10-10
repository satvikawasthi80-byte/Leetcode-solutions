from collections import deque

class Solution:
    def maximumMinutes(self, grid):
        m, n = len(grid), len(grid[0])
        INF = 10**9
        fire = [[INF] * n for _ in range(m)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fire[i][j] = 0
                    q.append((i, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0 and fire[nr][nc] == INF:
                    fire[nr][nc] = fire[r][c] + 1
                    q.append((nr, nc))

        def can_escape(wait):
            if wait >= fire[0][0]:
                return False

            q = deque([(0, 0, wait)])
            seen = {(0, 0)}

            while q:
                r, c, t = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    nt = t + 1

                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    if grid[nr][nc] == 2 or (nr, nc) in seen:
                        continue

                    if nr == m - 1 and nc == n - 1:
                        if nt <= fire[nr][nc]:
                            return True
                    elif nt < fire[nr][nc]:
                        seen.add((nr, nc))
                        q.append((nr, nc, nt))

            return False

        left, right = 0, m * n

        while left < right:
            mid = (left + right + 1) // 2
            if can_escape(mid):
                left = mid
            else:
                right = mid - 1

        if can_escape(left):
            return 10**9 if left == m * n else left
        return -1