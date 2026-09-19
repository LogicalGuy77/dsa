class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        left = [1]*n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
            else:
                left[i] = 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right = left[i+1] + 1
                left[i] = max(right, left[i])
            else:
                continue
        
        return sum(left)
        


ratings = [1,2,2]
obj = Solution()
print(obj.candy(ratings))