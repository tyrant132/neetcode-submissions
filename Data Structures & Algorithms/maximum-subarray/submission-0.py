class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = 0
        curSum = 0
        i,j = 0,0
        maximum = -math.inf
        n = len(nums)
        while i<n and j<n:
            maximum = max(maximum, nums[j])
            curSum += nums[j]
            if curSum>maxSum:
                maxSum = curSum
            if curSum<=0:
                curSum = 0
                i = j+1
            j += 1
        if maximum<=0:
            return maximum
        return maxSum
        