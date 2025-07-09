class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # 왼쪽 곱 계산
        left = 1
        for i in range(1, n):
            left *= nums[i - 1]
            res[i] = left

        # 오른쪽 곱을 곱해주기
        right = 1
        for i in reversed(range(n - 1)):
            right *= nums[i + 1]
            res[i] *= right

        return res
