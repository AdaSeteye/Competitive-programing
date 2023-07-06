class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        nums.sort()
        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] > mid:
                r = mid - 1
            else:
                l = mid + 1
        return l
