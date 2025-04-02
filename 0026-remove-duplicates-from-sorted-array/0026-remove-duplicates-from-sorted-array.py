class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 0
        while pointer < len(nums):
            i = pointer + 1
            while i < len(nums):
                if nums[pointer] == nums[i]:
                    nums.pop(i)
                else:
                    i += 1
            pointer += 1
        return len(nums)
