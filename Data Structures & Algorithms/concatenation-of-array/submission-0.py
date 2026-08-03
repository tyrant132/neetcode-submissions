class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        j = 2*n
        ans = [0]*j
        for _ in range(j):
            ans[_] = nums[_%n]
        return ans