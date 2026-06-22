class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        x = re.sub(r'[^A-Za-z0-9]','',s).lower()
        print(x)

        j = len(x) - 1
        
        for i in range(len(x)):
            if x[i] != x[j]:
                return False
            if i == j+1:
                return True
            j -= 1

        return True