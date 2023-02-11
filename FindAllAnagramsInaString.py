class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        count = Counter(p)
        lenP = len(p)
        for i, j in enumerate(s):
            count[j] -= 1
            if count[j] >= 0:
                lenP -= 1
            if i >= len(p):
                count[s[i - len(p)]] += 1
                if count[s[i - len(p)]] > 0:
                    lenP += 1
            if lenP == 0:
                result.append(i - len(p) + 1)
        return result
