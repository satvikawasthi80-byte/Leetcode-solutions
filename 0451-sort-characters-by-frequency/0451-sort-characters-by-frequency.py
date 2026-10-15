
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        result = ""

        for char, count in freq.most_common():
            result += char * count

        return result
