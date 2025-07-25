class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height)-1
        while left<right:
            x = right-left
            y = min(height[left], height[right])
            area =x*y
            if area > max_area:
                max_area = area
            if height[left] > height[right]:
                right -=1
            else:
                left +=1
        return max_area
            
