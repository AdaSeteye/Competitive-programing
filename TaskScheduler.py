class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=[value for value in Counter(tasks).values()]
        count.sort()
        max_freq=count.pop()
        room=max_freq-1
        idle=(room)*n
        while count and idle > 0:
            idle -= min(room, count.pop())
        return max(0,idle)+len(tasks)
