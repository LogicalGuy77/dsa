class Solution:
    def minOperation(self, s): 
        #code here
        i = 0
        ctr = 0 

        while i < len(s):
            if i>0 and s[0:i] == s[i:2*i]:
                ctr += 1
                i = 2*i
            else:
                i+=1
                ctr+=1
        return ctr
    
obj = Solution()
s = "abcabca"
print(obj.minOperation(s))
