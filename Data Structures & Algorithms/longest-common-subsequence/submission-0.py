class Solution:
    def solver(self, text1: str, text2: str, i: int,j:int, memo) -> int:
        if i>=len(text1) or j>=len(text2):
            return 0
        if memo[i][j]!=-1:
            return memo[i][j]
        if text1[i] == text2[j]:
            memo[i][j]=1+self.solver(text1, text2, i+1,j+1,memo)
            return memo[i][j]
        else:
            memo[i][j] = max(self.solver(text1, text2, i+1,j,memo),self.solver(text1, text2, i, j+1,memo))
            return memo[i][j]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        i,j = len(text1), len(text2)
        memo = [[-1]*j for k in range(i)]
        return self.solver(text1, text2,0,0,memo)
        