class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)  # O(n)

        # 가장 흔한 k개 추출 (최소 힙 사용)
        return [item for item, freq in heapq.nlargest(k, count.items(), key=lambda x: x[1])]
