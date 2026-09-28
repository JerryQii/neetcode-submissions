from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.dih = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dih[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        #binary search on 0<= ? <= timestamp
        res = self.dih.get(key)
        if res == None:
            return ''
        l,r = 0, len(res)-1
        ret = ''
        while l <= r:
            mid = (l+r)//2
            midt = res[mid][0]
            if midt <= timestamp:
                l = mid + 1
                ret = res[mid][1]
            elif midt > timestamp:
                r = mid - 1
        return ret

        
