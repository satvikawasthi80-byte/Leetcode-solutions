class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 10**9 + 7

        x = (1 << p) - 1
        y = (1 << p) - 2

        return (x * pow(y, (1 << (p - 1)) - 1, MOD)) % MOD