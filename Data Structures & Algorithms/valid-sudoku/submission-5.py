class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_set = set()
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == ".":
                    continue
                if board[i][j] in hash_set:
                    return False
                hash_set.add(board[i][j])
            hash_set.clear()
        
        for j in range(m):
            for i in range(n):
                if board[i][j] == ".":
                    continue
                if board[i][j] in hash_set:
                    return False
                hash_set.add(board[i][j])
            hash_set.clear()
        
        for x in range(0,m,3):
            for y in range(0,n,3):
                for i in range(x,x+3):
                    for j in range(y,y+3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in hash_set:
                            return False
                        hash_set.add(board[i][j])
                hash_set.clear()
        return True
            
                









