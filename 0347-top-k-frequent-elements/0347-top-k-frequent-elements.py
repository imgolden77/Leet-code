class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict()
        result=[]
        for num in nums:
            count[num]=count.get(num, 0) + 1
        for i in range(k):
            max_val = max(count.values())
            max_key = [k for k, v in count.items() if v == max_val]
            result.append(max_key[0])
            count.pop(max_key[0])
        return(result)