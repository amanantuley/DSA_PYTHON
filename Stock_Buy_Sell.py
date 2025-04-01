# Buy and sell stock to get maximum profit
def stock_price(prices):
    if not prices:
        return 0 
    
    min_price = float('inf')
    max_profit = 0 

    for price in prices:  
        min_price = min(min_price, price)  
        max_profit = max(max_profit, price - min_price)  

    return max_profit

# Example usage
price = [7, 1, 5, 3, 6, 4]
print(stock_price(price))  # Output: 5 (Buy at 1, Sell at 6)
