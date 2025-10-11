class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr =[]
        def backtrack(nums):

            if not nums:
                res.append(list(curr))
                print("results:", res)
                return

            for i in range(len(nums)):
                curr.append(nums[i])
                print("curr:", curr, "nums:", nums)
                backtrack(nums[:i]+nums[i+1:])
                curr.pop()

        backtrack(nums)
        print("res:", res)
        return res