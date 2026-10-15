class Solution: 
    def gettime(self, piles: List[int], v: int)-> int:
        res = 0
        for i in piles:
            time = math.ceil(i/v) #math.ceil()
            res += time
        return res

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # input: list of positive intergers, steps to ceiling division all the values in list
        # output: the minimum value to fnish decreasing the list within h steps
        # 1 < output <max(piles)
        # 
        left, right = 1, max(piles) 
        res = right
        while left <= right:
            mid = (left + right) // 2
            time = self.gettime(piles, mid)
            if time <= h:
                right = mid - 1
                res = mid
            else:
                left = mid +1
        return res