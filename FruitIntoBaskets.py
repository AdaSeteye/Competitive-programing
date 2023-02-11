class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        numFruits = 0
        count = collections.defaultdict(int)
        l = 0
        for r, t in enumerate(fruits):
            count[t] += 1
            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
            numFruits = max(numFruits, r - l + 1)
        return numFruits
