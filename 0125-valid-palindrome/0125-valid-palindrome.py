class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= ''.join([c for c in s if c.isalpha() or c.isdigit()])
        s= s.lower()
        # print(s)
        s_list=list(s)
        for i in range(len(s)):
            if len(s_list)== 0 or len(s_list)== 1:
                return True
            elif s_list[i] != s_list[-i-1]:
                # print(i, s_list[i], s_list[-i-1])
                return False
        return True