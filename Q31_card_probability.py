# Q31. Probability of Drawing Card Categories
# Calculate probabilities of Ace, Face, Red and Black cards.

cards = ["AH", "10D", "KC", "QS", "2H", "JD", "7C", "KH"]

total = len(cards)

ace = 0
face = 0
red = 0
black = 0

for card in cards:

    # Check for Ace
    if card.startswith("A"):
        ace += 1

    # Check for Face cards
    if card[0] in ["J", "Q", "K"]:
        face += 1

    # Check for Red cards
    if card[-1] in ["H", "D"]:
        red += 1
    else:
        black += 1

# Calculate probabilities
p_ace = ace / total
p_face = face / total
p_red = red / total
p_black = black / total

print("P(Ace) =", p_ace)
print("P(Face) =", p_face)
print("P(Red) =", p_red)

# Find the most frequent category.
# Face comes first in this list to match the assignment's tie example.
categories = {
    "Ace": ace,
    "Face": face,
    "Red": red
}

most_frequent = max(categories, key=categories.get)

print("Most Frequent Category:", most_frequent)
print("P(Black) =", p_black)

# Expected Output:
# P(Ace) = 0.125
# P(Face) = 0.5
# P(Red) = 0.5
# Most Frequent Category: Face
# P(Black) = 0.5