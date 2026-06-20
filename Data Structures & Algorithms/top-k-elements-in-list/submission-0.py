class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        has = dict()
        for num in nums:
            if num in has:
                has[num] = has[num] + 1
            else: has[num] = 1
        max = 0
        maxi = 0
        ans = [0] * k
        print(has)
        for i in range(k):
            for key, val in has.items():
                if val > max:
                    max = val
                    maxi = key
            ans[i] = maxi
            print(maxi)
            del has[maxi]
            max = 0
        return ans