class Solution:
    def getMaxLen(self, nums):
        pos = neg = ans = 0

        for x in nums:
            if x == 0:
                pos = neg = 0

            elif x > 0:
                pos += 1
                if neg > 0:
                    neg += 1

            else:
                old_pos = pos
                pos = neg + 1 if neg > 0 else 0
                neg = old_pos + 1

            ans = max(ans, pos)

        return ans
        