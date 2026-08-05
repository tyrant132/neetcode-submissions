class Solution:
    def isValid(self, n, piles, h) -> bool:
        length = len(piles)
        s = 0
        for i in range(length):
            if piles[i]%n==0:
                s += piles[i]/n
            else:
                s += piles[i]//n+1
        if s<=h:
            return True
        return False
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = sum(piles)
        ans = high
        while low<=high:
            mid = low + (high-low)//2
            if self.isValid(mid,piles,h):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans