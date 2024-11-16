class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = [c for c in s.lower() if c.isalnum()]
        print(s)
        return s == s[::-1]