class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        boolean_list = []
        for i in range(len(l)):
            temp = 1
            temp_list = []
            for j in range(l[i], r[i] + 1):
                temp_list.append(nums[j])
            temp_list.sort()
            com_diff = temp_list[1] - temp_list[0]
            for k in range(len(temp_list) - 1):
                if temp_list[k+1] - temp_list[k] != com_diff:
                    temp -= 1
            if temp < 1:
                boolean_list.append(False) 
            else:
                boolean_list.append(True)
        return boolean_list
