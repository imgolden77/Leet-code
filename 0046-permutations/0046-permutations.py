class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        current_permutation = []
        def backtrack(nums):
            if not nums:
                results.append(list(current_permutation))
                return

            for i in range(len(nums)):
                current_permutation.append(nums[i])
                backtrack(nums[:i] + nums[i+1:])
                current_permutation.pop()

        backtrack(nums)
        return results