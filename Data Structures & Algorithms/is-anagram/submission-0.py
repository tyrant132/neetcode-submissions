class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        n = len(s)
        memo = [0]*26
        for _ in range(n):
            memo[ord(s[_]) - ord('a')] += 1
        for _ in range(n):
            memo[ord(t[_])-ord('a')] -= 1
            if memo[ord(t[_])-ord('a')]<0:
                return False
        return True
        