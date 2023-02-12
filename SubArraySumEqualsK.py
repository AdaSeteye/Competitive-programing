class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        tempSum = 0
        prefixSum = { 0:1 }
        for i in nums:
            tempSum += i
            difference = tempSum - k
            result += prefixSum.get(difference, 0)
            prefixSum[tempSum] = 1 + prefixSum.get(tempSum, 0)
        return result
