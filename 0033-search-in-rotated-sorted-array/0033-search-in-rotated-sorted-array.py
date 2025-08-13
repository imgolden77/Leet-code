class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right= 0, len(nums)-1

        while left<=right:
            mid=(left+right)//2
            print("DEBUG0:", left, mid, right)
            if nums[mid]==target:
                return mid
            if nums[left]<= nums[mid]:
                if nums[left]<=target<nums[mid]:
                    right= mid -1
                    print("DEBUG1:", left, mid, right)
                else:
                    left= mid+1
                    print("DEBUG2:", left, mid, right)
            else:
                if nums[mid]< target<=nums[right]:
                    left=mid+1
                    print("DEBUG3:", left, mid, right)
                else:
                    right= mid-1
                    print("DEBUG4:", left, mid, right)
        
        return -1
            

                
