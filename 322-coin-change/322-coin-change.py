class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mincoins = [float('inf') for _ in range(amount+1)]
        mincoins[0] = 0
        for coin in coins:
            for i in range(1,amount+1):
                if coin == i:
                    mincoins[i] = 1
                elif coin > i:
                    mincoins[i] = mincoins[i]
                else:
                    mincoins[i] = min(mincoins[i-coin] + 1, mincoins[i])
        return mincoins[-1] if mincoins[-1] != float('inf') else -1

                
                
            