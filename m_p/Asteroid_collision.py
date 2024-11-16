class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                
                diff = a + stack[-1]

                if diff < 0:
                    stack.pop()
                    continue
                elif diff > 0:
                    a = 0
                    break
                elif diff == 0:
                    a = 0
                    stack.pop()
            
            if a != 0:
                stack.append(a)

        return stack

