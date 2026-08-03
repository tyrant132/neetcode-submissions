class Solution:
    def solver(self, cost: List[int], idx: int, memo: List[int]) -> int:
        if idx>=len(cost):
            return 0
        if memo[idx]!=-1:
            return memo[idx]
        memo[idx] = cost[idx]+min(self.solver(cost, idx+1,memo),self.solver(cost, idx+2,memo))
        return memo[idx]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)==2:
            return min(cost[0],cost[1])
        memo = [-1] * len(cost)
        return min(self.solver(cost,0,memo),self.solver(cost,1,memo))