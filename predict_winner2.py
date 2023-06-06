class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def helper(start, end):
            if start == end:
                return nums[start]
            chooseStart = nums[start] - helper(start + 1, end)
            chooseEnd = nums[end] - helper(start, end - 1)
            return max(chooseStart, chooseEnd)
    
        return helper(0, len(nums) - 1) >= 0
