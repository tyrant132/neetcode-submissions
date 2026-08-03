class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        memo = [0]*(n-1)
        memo[0] = nums[0]
        memo[1] = max(nums[0],nums[1])
        for _ in range(2,n-1):
            memo[_] = max(memo[_-2]+nums[_],memo[_-1])
        memo2 = [0]*(n-1)
        memo2[0] = nums[1]
        memo2[1] = max(nums[1],nums[2])
        for _ in range(2,n-1):
            memo2[_] = max(memo2[_-2]+nums[_+1],memo2[_-1])
        return max(memo[n-2],memo2[n-2])
        