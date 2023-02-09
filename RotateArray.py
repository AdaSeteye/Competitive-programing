class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reversing(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
        l = 0
        r = len(nums) - 1
        k = k%len(nums)
        reversing(l, r)
        reversing(l, k-1)
        reversing(k,r)
