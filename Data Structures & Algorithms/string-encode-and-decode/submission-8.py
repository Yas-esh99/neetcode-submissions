class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(str(len(s)) + "#" + s)
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        p  = 0
        out = []
        
        while p < len(s):
            j = p
            while s[j] != "#":
                j+=1
            lnth = int(s[p:j])
            p = j+1

            out.append(s[p:p+lnth])
            p += lnth
            
            

        return out
            
            