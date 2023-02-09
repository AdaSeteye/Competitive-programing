class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        count = 0
        right = len(people) - 1

        while left <= right:
            temp = limit - people[right]
            right-=1
            count+=1
            if left <= right and temp >= people[left]:
                left+=1
        return count
