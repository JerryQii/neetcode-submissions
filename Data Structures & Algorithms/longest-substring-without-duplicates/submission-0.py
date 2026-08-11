class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        longest = 0
        seen = set()
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                longest = max(longest,r-l+1)
                r += 1
            else:
                seen.remove(s[l])
                l+=1
        return longest


