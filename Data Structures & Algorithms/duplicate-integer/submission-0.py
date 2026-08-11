class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in nums:
            if dic.get(i) == None:
                dic.update({i:1})
            else:
                 return True
        return False

         