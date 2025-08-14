from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))  # 정렬된 문자열을 키로
            anagrams[key].append(word)

        return list(anagrams.values())