class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prd = 1
        for n in nums:
            total_prd *= n
        out = []
        tmp_prd = 1
        for i,n in enumerate(nums):
            if n == 0:
                for j,m in enumerate(nums):
                    if i == j:
                        continue
                    tmp_prd *= m
                out.append(tmp_prd)
                continue
            out.append(total_prd//n)
            
        return out