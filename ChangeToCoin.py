# Set change
change = 5700

# Set list of coin amounts
coins = [1000, 500, 200, 100]

# Make a dict to store the number of coins
coin_amount = {}

# Calculate the change in form of multiple coins
for coin in coins:
    
    # Change divided by coin amount (and rounded down)
    numOfCoins = change // coin
    
    # Add coin:amount to dict
    coin_amount[coin] = numOfCoins
    
    # Decrease the change for further calculation
    change -= numOfCoins * coin
    
# Display the change in amount of coins :D
for coin, num in coin_amount.items():
    print(f'{num} x Rp{coin}')