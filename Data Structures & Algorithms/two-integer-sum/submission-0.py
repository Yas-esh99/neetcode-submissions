class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasmap = {}
        i = 0
        for num in nums:
            numToSearch = target - num
            if numToSearch not in hasmap:
                hasmap[num] = i
            else: return [hasmap[numToSearch],i]
            i = i + 1
        