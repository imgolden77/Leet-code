class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr =[]
        def backtrack(nums):

            if not nums:
                res.append(list(curr))
                return

            for i in range(len(nums)):
                curr.append(nums[i])
                backtrack(nums[:i]+nums[i+1:])
                curr.pop()

        backtrack(nums)
        return res