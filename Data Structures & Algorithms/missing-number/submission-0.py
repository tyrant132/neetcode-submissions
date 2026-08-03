class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = 0
        n = len(nums)
        for _ in range(n):
            s += nums[_]
        return ((n*(n+1))-2*s)//2