class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= ''.join([c for c in s if c.isalpha() or c.isdigit()])
        s= s.lower()
        if len(s)== 0 or len(s)== 1:
            return True
        for i in range(len(s)):
            if s[i] != s[-i-1]:
                return False
        return True