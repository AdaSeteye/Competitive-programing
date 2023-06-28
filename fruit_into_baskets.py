class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r = 0, 0
        res = 0
        counter = {}
        while r < len(fruits):
            counter[fruits[r]] = 1 + counter.get(fruits[r], 0)

            while len(counter) > 2:
                counter[fruits[l]] -= 1
                if counter[fruits[l]] == 0:
                    counter.pop(fruits[l])
                l += 1
            r += 1
            res = max(res, r - l)
        return res
