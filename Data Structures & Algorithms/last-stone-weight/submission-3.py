class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.append(0)
        heapq.heapify_max(stones)

        while len(stones) > 1:
            first = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)
            if second < first:
                heapq.heappush_max(stones, first - second)

        return abs(stones[0])