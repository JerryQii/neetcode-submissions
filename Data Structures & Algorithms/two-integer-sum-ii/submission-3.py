class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lptr, rptr = 0, len(numbers) - 1
        Sum = numbers[lptr] + numbers[rptr]
        while Sum != target : 
            if Sum < target :
                lptr += 1
            if Sum > target :
                rptr -= 1
            Sum = numbers[lptr] + numbers[rptr]
        return [lptr + 1, rptr + 1]