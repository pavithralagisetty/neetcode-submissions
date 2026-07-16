class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        d=[(0,1),(1,0),(-1,0),(0,-1)]
        m=len(board)
        n=len(board[0])
        def dfs(i,j,c):
            
            if c==len(word):
                print(c)
                return True
            
            visit.add((i,j))
            for dx,dy in d:
                a=dx+i
                b=dy+j
                if 0<=a<m and 0<=b<n and (a,b) not in visit and board[a][b]==word[c]:
                    if dfs(a,b,c+1):
                        return True
                    
                    #visit.add((a,b))
            visit.remove((i,j))
            #return False


        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    visit=set()
                    if dfs(i,j,1):
                        return True
        return False
   
