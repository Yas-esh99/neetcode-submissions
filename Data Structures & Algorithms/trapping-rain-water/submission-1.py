class Solution:
    def trap(self, height: List[int]) -> int:
        
        i = 0
        j = len(height) - 1

        maxR = height[j]
        maxL = height[i]

        ans = 0

        while i <= j:

            if height[i] <= height[j]:
                maxL = max(height[i],maxL)
                a = maxL - height[i]
                if a > 0:
                    ans += a
                i +=1 
            
            else:
                maxR = max(height[j],maxR)
                a = maxR - height[j]
                if a > 0:
                    ans += a
                j -=1 

        return ans