class Solution:
    def climbStairs(self, n: int) -> int:
        count = {}
        count[0]=0
        count[1]=1
        count[2]=2
        if n < 3:
            return count[n]
        for i in range(3,n+1):
            count[i] = count[i-1]+count[i-2] 
        return count[n]
        
        