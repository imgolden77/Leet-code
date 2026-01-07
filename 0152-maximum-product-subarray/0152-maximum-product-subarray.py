class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax= 1
        curMin= 1
        res = -11

        for num in nums :
            prevMax = curMax 
            prevMin = curMin
            curMax = max(num, num * prevMax, num * prevMin)
            curMin = min(num, num * prevMax, num * prevMin)
            res = max(curMax, res)     
        
        return res
