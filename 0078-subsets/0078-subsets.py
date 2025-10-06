class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res= [[]]
    
        for idx in range(n):
            subsets=[]
            for subset in res:
                curr = subset.copy()
                curr.append(nums[idx])
                subsets.append(curr)
            
            res.extend(subsets)
        
        return res