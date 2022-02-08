class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def helper(coins, amount, memo=dict()):
            if amount in memo: return memo[amount]
            if amount == 0: return 0
            if amount < 0: return -1

            shortest = -1

            for coin in coins:
                rem = helper(coins, amount - coin, memo)
                if rem != -1:
                    curr = rem + 1
                    if shortest == -1 or curr < shortest:
                        shortest = curr
            memo[amount] = shortest
            return shortest
        
        return helper(coins, amount)