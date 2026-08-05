class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        j = n-1
        memo = [-1]*2
        mydict = {}
        for i in range(n):
            if mydict.get(target-nums[i]) is not None:
                memo[0] = mydict.get(target-nums[i])
                memo[1] = i
                return memo
            else:
                mydict[nums[i]] = i
        return memo
        