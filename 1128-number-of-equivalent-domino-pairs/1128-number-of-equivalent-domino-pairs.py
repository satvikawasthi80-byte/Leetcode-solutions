class Solution:
    def numEquivDominoPairs(self, dominoes):
        count = {}
        ans = 0

        for a, b in dominoes:
            key = (min(a, b), max(a, b))

            if key in count:
                ans += count[key]

            count[key] = count.get(key, 0) + 1

        return ans