class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        pre,suf = [],[]
        premax,sufmax = -1,-1
        for i in range(0,len(height)):
            premax = max(premax,height[i])
            pre.append(premax)
        for i in range(len(height)-1,-1,-1):
            sufmax = max(sufmax,height[i])
            suf.append(sufmax)
        suf = suf[::-1]
        for i in range(0,len(height)):
            water = min(pre[i],suf[i]) - height[i]
            if water > 0:
                res += water
        return res