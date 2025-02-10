class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_list=list(ransomNote)
        magazine_list=list(magazine)
        for i in ransomNote_list:
            if i in magazine_list:
                magazine_list.remove(i)
            else:
                return False
        return True   