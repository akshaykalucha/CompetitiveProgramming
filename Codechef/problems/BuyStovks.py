class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ss = []
        for i in range(len(prices)):
            if i+1 == len(prices):
                break
            curr = prices[i:]
            for j in range(1, len(curr)):
                sell = curr[j] - prices[i]
                ss.append(sell)
        if len(ss) > 0:
            if max(ss) > 0:
                return max(ss)
            else:
                return 0
        else:
            return 0
            