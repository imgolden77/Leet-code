class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = []
        max_s = 0
        for i in s:
            if i not in h:
                h.append(i)
                print(h)
            else:
                # max_s = max(max_s, len(h))
                h=h[h.index(i)+1:]
                h.append(i)
            max_s = max(max_s, len(h))
        
        return max_s
