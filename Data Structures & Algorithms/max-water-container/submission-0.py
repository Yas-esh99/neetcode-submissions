class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxi = 0
        left = 0
        right = len(heights) -1
        area = 0
        while right > left:

            if heights[right] >= heights[left]:
                area = heights[left]*(right-left)
                left += 1

            else :
                area = heights[right]*(right- left)
                right -= 1

            maxi = max(area,maxi)
        return maxi