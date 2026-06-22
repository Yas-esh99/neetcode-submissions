class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        numSet = set(nums)

        maxi = 1
        for num in numSet:

            currentStreak = 1
            currentNum = num
            if num - 1 not in numSet:
                while currentNum + 1 in numSet:
                    currentStreak += 1
                    currentNum += 1

            maxi = max(currentStreak,maxi)
        
        return maxi