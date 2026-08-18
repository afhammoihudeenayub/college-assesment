import random

# Create 52-card deck using list comprehension
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

deck = [rank + " of " + suit for rank in ranks for suit in suits]

# Get number of players
while True:
    try:
        players = int(input("Enter number of players: "))

        if players > 0 and 52 % players == 0:
            break
        else:
            print("Enter a positive number that divides 52 evenly.")

    except ValueError:
        print("Please enter a number.")

# Shuffle deck
random.shuffle(deck)

# Give cards equally
cards_each = 52 // players
hands = []

for i in range(players):
    hands.append(deck[i * cards_each:(i + 1) * cards_each])

scores = [0] * players

# Play rounds
for round_no in range(1, cards_each + 1):

    print("\nRound", round_no)

    # Select one random card from each player's hand
    played_cards = []

    for i in range(players):
        card = random.choice(hands[i])
        hands[i].remove(card)
        played_cards.append(card)
        print("Player", i + 1, "played:", card)

    # Select winner
    while True:
        try:
            winner = int(input("Enter round winner (player number): "))

            if 1 <= winner <= players:
                break
            else:
                print("Invalid player number.")

        except ValueError:
            print("Please enter a number.")

    scores[winner - 1] += 1

# Final result
print("\nFinal Scores:")

for i in range(players):
    print("Player", i + 1, ":", scores[i])

highest = max(scores)

winners = []

for i in range(players):
    if scores[i] == highest:
        winners.append(i + 1)

if len(winners) == 1:
    print("Overall Winner: Player", winners[0])
else:
    print("It's a tie between:", winners)