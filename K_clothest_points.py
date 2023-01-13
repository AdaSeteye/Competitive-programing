class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lst=[]
        lst2=[]
        for i in range(len(points)):
            points[i].append(points[i][0]**2 + points[i][1]**2)
            lst.append(points[i])
        lst = sorted(lst, key = lambda x: x[2])
        for j in range(k):
            lst[j].pop()
            lst2.append(lst[j]) 
        return lst2
