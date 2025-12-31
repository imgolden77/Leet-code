class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        max_len = 0
        seen = {}

        for i, char in enumerate(s):
            if char not in seen:
                seen[char] = 1
            else:
                seen[char] += 1
            max_val = max(list(seen.values()))
            if i - start - max_val + 1 <= k:
                max_len = max(max_len, i - start + 1)
            else:
                seen[s[start]] -= 1
                start += 1

        return max_len
