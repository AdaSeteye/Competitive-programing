class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        i, j = 0, len(cardPoints) - k
        total = sum(cardPoints[j:])
        result = total
        for _ in range(k):
            total += cardPoints[i] - cardPoints[j]
            result = max(result, total)
            i += 1
            j += 1
        return result
