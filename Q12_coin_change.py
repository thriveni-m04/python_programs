# Q12. Coin Change
# Find the minimum number of coins needed to make the given amount.

coins = [1, 2, 5]
amount = 11

# Create a list to store minimum coins required for each amount.
# A large value means the amount cannot be formed yet.
dp = [float('inf')] * (amount + 1)

# Zero coins are needed to make amount zero.
dp[0] = 0

# Check every amount from 1 to the required amount.
for i in range(1, amount + 1):

    # Try every available coin.
    for coin in coins:

        if coin <= i:
            dp[i] = min(dp[i], dp[i - coin] + 1)

# Check whether the amount can be formed.
if dp[amount] == float('inf'):
    print("Minimum Coins:", -1)
else:
    print("Minimum Coins:", dp[amount])