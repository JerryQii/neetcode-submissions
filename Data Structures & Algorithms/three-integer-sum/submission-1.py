class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        indexset = set()
        for i in range(0, len(nums)):
            target = 0 - nums[i]
            hashmap = {}
            for j in range(i+1, len(nums)):
                target2 = target - nums[j]
                if target2 not in hashmap:
                    hashmap[nums[j]] = j
                else:
                    k = hashmap[target2]
                    indices = tuple(sorted([nums[i], nums[j], nums[k]]))
                    if indices in indexset:
                        continue
                    res.append([nums[i], nums[j], nums[k]])
                    indexset.add(indices)
        return res