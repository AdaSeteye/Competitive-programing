class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n - 2, -1, -1):
            k = i + 1

            while temperatures[i] >= temperatures[k] and res[k] > 0:
                print(i)
                k += res[k]

            if temperatures[k] > temperatures[i]:
                res[i] = k - i

        return res
