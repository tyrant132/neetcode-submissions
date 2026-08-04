class Solution:
    sys.setrecursionlimit(20000) # Just look out for the default recursion depth which is 1000 if doing memoization
    def solver(self, coins: List[int], amount: int, idx: int, memo) -> int:
        if amount==0:
            return 0
        if idx==len(coins):
            return math.inf
        if memo[idx][amount]!=-1:
            return memo[idx][amount]
        skip = self.solver(coins, amount, idx+1,memo)
        take = math.inf
        if amount>=coins[idx]:
            take = 1+self.solver(coins, amount-coins[idx],idx,memo)
        memo[idx][amount] = min(skip,take)
        return memo[idx][amount]
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        m = len(coins)
        # memo = [[-1]*(amount+1) for i in range(m)]
        # ans = self.solver(coins, amount, 0,memo)
        # if ans>=math.inf:
        #     return -1
        # return ans
        memo = [float('inf') for i in range(amount+1)]
        memo[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if i-coin>=0:
                    memo[i] = min(memo[i],memo[i-coin]+1)
        return memo[amount] if memo[amount] != float('inf') else -1

