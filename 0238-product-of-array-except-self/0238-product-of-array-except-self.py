class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]
        right=[]
        res=[]
        a=1
        b=1
        for i in range(1, len(nums)):
            a = a * nums[i-1]
            left.append(a)
        for i in reversed(range(len(nums))):
            if i == len(nums)-1:
                b = b * 1
                right.append(b)
            else:
                b = b * nums[i+1]
                right.append(b)
        right.reverse()
        return [left[i] * right [i] for i in range(len(nums))]

