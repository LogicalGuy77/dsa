from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        print(asteroids)
        
        stk = []
        for i in asteroids:
            while stk and i < 0 < stk[-1]:
                if stk[-1] < -i:
                    stk.pop()
                    continue
                if stk[-1] == -i:
                    stk.pop()
                break
            # if break encounterd in loop then else runs
            else:
                stk.append(i)    
        
        print(stk)



asteroids = [8, -8]
obj = Solution()
obj.asteroidCollision(asteroids)


    # def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    #     print(asteroids)
    #     n= len(asteroids)
    #     i = n-1

    #     while i>0:
    #         # if moving in same direction, do nothing
    #         if asteroids[i]>0 and asteroids[i-1]>0 or asteroids[i]<0 and asteroids[i-1]<0:
    #             continue
            

    #         # if moving in oposite direction will never collide
    #         # if i-1 is -ve and i is +ve
    #         if asteroids[i-1] < 0 and asteroids[i] > 0:
    #             continue
            
    #         # if i-1 is +ve and i is -ve // COLLISION   
    #         if asteroids[i-1] > 0 and asteroids[i] < 0:
    #             # if equal
    #             if asteroids[i-1]+asteroids[i] == 0:
    #                 asteroids[i-1] = 0
    #                 asteroids[i] = 0
    #                 continue
    #             asteroids[i-1] = asteroids[i] if asteroids[i]*-1 > asteroids[i-1] else asteroids[i-1]

    #         asteroids[i] = 0
    #         i -= 1
    #         print(asteroids)

    #     ans = []

    #     for i in asteroids:
    #         if i!=0:
    #             ans.append(i)

    #     print(ans)