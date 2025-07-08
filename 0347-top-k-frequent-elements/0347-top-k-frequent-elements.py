class Solution:
    def topKFrequent(self, nums, k):
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        # 버킷: index = 등장 횟수, 값 = 숫자 목록
        bucket = [[] for _ in range(len(nums)+1)]
        for num, freq in count.items():
            bucket[freq].append(num)

        result = []
        # 등장 횟수가 높은 것부터 거꾸로 순회
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result