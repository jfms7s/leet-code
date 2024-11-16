class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        s = [c for c in s if c.isalnum()]
        print("".join(s),"".join(reversed(s)))
        return "".join(s) == "".join(reversed(s))