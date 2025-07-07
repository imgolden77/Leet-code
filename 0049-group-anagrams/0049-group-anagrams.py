from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            count = [0] * 26  # 알파벳 26개
            for c in word:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)  # 리스트는 키로 못 쓰니 튜플로
            anagrams[key].append(word)

        return list(anagrams.values())
