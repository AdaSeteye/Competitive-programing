class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            while stack and asteroids[i] < 0 and stack[-1] > 0:
                diff = asteroids[i] + stack[-1]
                if diff < 0: 
                    stack.pop()
                elif diff > 0:
                    asteroids[i] = 0
                else:
                    asteroids[i] = 0
                    stack.pop()
            if asteroids[i]:
                stack.append(asteroids[i])
        return stack
