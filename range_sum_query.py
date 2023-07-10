class NumArray:

    def __init__(self, nums: List[int]):
        self.preSum = []
        self.preSum.append(nums[0])
        for i in range(1, len(nums)):
            self.preSum.append(self.preSum[i - 1] + nums[i])
        
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.preSum[right]
        return self.preSum[right] - self.preSum[left - 1]
