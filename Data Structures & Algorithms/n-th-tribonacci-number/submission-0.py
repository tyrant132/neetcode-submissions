class Solution:
    def tribonacci(self, n: int) -> int:
        prev = 1
        prev2 = 1
        prev3 = 0
        if n<2:
            return n
        if n==2:
            return 1
        cur = 0
        for _ in range(3,n+1):
            cur = prev+prev2+prev3
            prev3 = prev2
            prev2 = prev
            prev = cur
        return cur
        