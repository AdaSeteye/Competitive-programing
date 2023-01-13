class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        temp_list = []
        target_list = []
        for i in count:
            temp_list.append([i, count[i]])
        temp_list = sorted(temp_list, key = lambda x: x[1], reverse = True)
        for j in range(k):
            target_list.append(temp_list[j][0])
        return target_list
