
class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(strength)

        left = [-1] * n
        right = [n] * n
        stack = []

        for i in range(n):
            while stack and strength[stack[-1]] >= strength[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []

        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] > strength[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = (prefix[i] + strength[i]) % MOD

        prefix2 = [0] * (n + 2)
        for i in range(n + 1):
            prefix2[i + 1] = (prefix2[i] + prefix[i]) % MOD

        ans = 0

        for i in range(n):
            l = left[i]
            r = right[i]

            left_count = i - l
            right_count = r - i

            total_right = (prefix2[r + 1] - prefix2[i + 1]) % MOD
            total_left = (prefix2[i + 1] - prefix2[l + 1]) % MOD

            contribution = (
                total_right * left_count
                - total_left * right_count
            ) % MOD

            ans = (ans + strength[i] * contribution) % MOD

        return ans
