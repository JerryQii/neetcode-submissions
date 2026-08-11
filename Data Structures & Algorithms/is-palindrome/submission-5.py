class Solution:
    def isPalindrome(self, s: str) -> bool:
        NewS = ''
        for c in s:
            if c.isalnum():
                NewS += c.lower()
        return NewS == NewS[::-1]
