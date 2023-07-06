class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        while l <= h:
            mid = l + (h - l)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                h = mid - 1
            elif target > nums[mid]:
                l = mid + 1
        return l
