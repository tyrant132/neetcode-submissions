class Solution:
    def solver(self, nums: List[int], idx: int, li: List[int], ans, target: int) -> None:
        if target == 0:
            ans.append(li[:]) #Copy of li to be added in the ans
            return
        if idx == len(nums):
            return
        if nums[idx]<=target:
            li.append(nums[idx])
            self.solver(nums,idx,li,ans,target-nums[idx])
            li.pop()
        self.solver(nums,idx+1,li,ans,target)
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        li = []
        ans = []
        self.solver(nums, 0, li, ans, target)
        return ans