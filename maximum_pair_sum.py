class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        max_sum = []
        for i in range(n//2):
            max_sum.append(nums[i] + nums[n - i - 1])
        max_sum.sort()
        return max_sum[-1]
