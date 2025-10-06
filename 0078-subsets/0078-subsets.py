class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res= [[]]
        def dp(idx):
            for r in res:
                curr = r.copy()
                if nums[idx] not in curr:
                    curr.append(nums[idx])
                    print("curr:", curr)
                    res.append(curr)
                    print("res:", res)

            
        for idx in range(n):
            dp(idx)
        
        return res