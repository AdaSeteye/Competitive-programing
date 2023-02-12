class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        n = len(chalk)
        if k % total == 0:
            return 0
        temp = k % total
        for i in range(n):
            temp -= chalk[i]
            if temp < 0:
                return i
