class Solution:
    def check(self, i, j, board, word, lenWord,string,visited):
        if lenWord == 0:
            if string == word:
                return True
            return False
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        for di in directions:
            nx, ny = i+di[0],j+di[1]
            if nx<len(board) and nx >= 0 and ny >= 0 and ny<len(board[0]) and visited[nx][ny] == -1:
                if board[nx][ny] == word[len(word)-lenWord]:
                    string += board[nx][ny]
                    visited[nx][ny] = 1
                    a = self.check(nx,ny,board,word,lenWord-1,string,visited)
                    if a == True:
                        return True
                    string = string[:-1]
                    visited[nx][ny] = -1
        return False
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0]) 
        lenWord = len(word)
        for i in range(m):
            for j in range(n):
                string = ""
                visited = [[-1]*n for k in range(m)]
                if board[i][j] == word[0]:
                    string = word[0]
                    visited[i][j] = 1
                if self.check(i,j,board,word,lenWord-1,string,visited):
                    return True
        return False
          