class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        mid= len(nums)//2
        while mid > 0:
            if nums[mid] != target:
                mid -=1
            else:
                return mid
        while mid < len(nums):
            if nums[mid] != target:
                mid+=1
            else:
                return mid
        return -1
            

                
