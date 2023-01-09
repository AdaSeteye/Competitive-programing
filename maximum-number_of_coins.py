class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        test = len(piles)//3
        sum = i = j = 0
        while test != j:
            i+=2
            sum+= piles[len(piles) - i]
            j+=1
        return sum
