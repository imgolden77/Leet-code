class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        record = Counter(nums)
        heap = [(-freq, num) for num, freq in record.items()]
        heapq.heapify(heap)
        ret = []
        while k > 0:
            freq, num = heapq.heappop(heap)
            ret.append(num)
            k -= 1

        return ret