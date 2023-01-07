class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        f, l = 0, len(nums)-1
        nums.sort()
        nums_temp=[]
        while len(nums) != len(nums_temp):
            nums_temp.append(nums[f])
            f+=1

            if f <= l:
                nums_temp.append(nums[l])
                l-=1
        return nums_temp
