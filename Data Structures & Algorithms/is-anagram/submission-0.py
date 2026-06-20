class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slst = list(s)
        rlst = list(t)
        if len(slst) != len(rlst):
            return False
        for c in slst:
            if c in rlst:
                rlst.remove(c)
            else: return False
        return True