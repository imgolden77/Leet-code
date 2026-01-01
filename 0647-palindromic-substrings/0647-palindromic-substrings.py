class Solution:
    def countSubstrings(self, s: str) -> int:
        total_count = 0

        def expand(left, right):
            local_count = 0
            while left>=0 and right< len(s) and s[left] == s[right]:
                local_count += 1
                left -= 1
                right += 1
            return local_count

        for i in range(len(s)):
            total_count += expand(i, i)
            total_count += expand(i, i+1)
        
        return total_count

            
