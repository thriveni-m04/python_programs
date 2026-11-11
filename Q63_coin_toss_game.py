
# Q63: Debugging a Coin-Toss Game

import random

# Get the player's prediction
guess = input("Predict the coin toss (heads/tails): ").lower()

# Validate the input
if guess not in ["heads", "tails"]:
    print("Invalid prediction. Enter heads or tails.")

else:

    # Generate a random coin toss
    toss = random.choice(["heads", "tails"])

    # Check the game result
    result = (guess == toss)

    # Pause execution for debugging
    breakpoint()

    # Display the result
    print("Your prediction:", guess)
    print("Coin toss result:", toss)

    if result:
        print("Congratulations! Your prediction is correct.")
    else:
        print("Sorry! Your prediction is incorrect.")
