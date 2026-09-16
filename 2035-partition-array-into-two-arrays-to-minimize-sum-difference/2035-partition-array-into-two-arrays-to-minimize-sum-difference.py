class Solution:
    def minimumDifference(self, nums):
        n = len(nums) // 2
        total = sum(nums)

        def gen(arr):
            d = [[] for _ in range(n + 1)]
            for mask in range(1 << n):
                s = 0
                cnt = 0
                for i in range(n):
                    if mask >> i & 1:
                        s += arr[i]
                        cnt += 1
                d[cnt].append(s)
            return d

        A = gen(nums[:n])
        B = gen(nums[n:])

        ans = float('inf')

        for k in range(n + 1):
            B[k].sort()
            for x in A[k]:
                target = total / 2 - x

                import bisect
                j = bisect.bisect_left(B[n-k], target)

                for p in [j-1, j]:
                    if 0 <= p < len(B[n-k]):
                        ans = min(ans, abs(total - 2*(x + B[n-k][p])))

        return ans