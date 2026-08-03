class Solution:
    def reverseBits(self, n: int) -> int:
        cnt = 32
        ans = 0
        for _ in range(cnt):
            ans = ans<<1
            ans+=n&1
            n = n>>1
        return ans
