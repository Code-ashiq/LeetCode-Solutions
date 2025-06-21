# problem 121.Best Time to Buy and Sell Stock, Level : Easy

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1  # initialize two pointers: l is buy, r is sell
        max_profit = 0 # variable to store the maximum profit found
        
        # Loop until r pointer reaches the end of the list
        while r < len(prices):

            if prices[l] < prices[r]:
                profit = prices[r] - prices[l] # calculate the profit
                max_profit = max(max_profit, profit) # update max_profit if the profit is higher
            else:
                # if the price at r is less than or equal to price at l
                # it means a better buying opportunity, so move l to r
                l = r
            r += 1 # always move the right pointer forward
        return max_profit
    
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))