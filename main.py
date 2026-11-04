
from player import Player

print("Welcome to Two-Deck War!")

# Create two players with their own decks of cards

player1 = Player("Player1")

player2 = Player("Player2")

# Shuffle both decks so the cards are in a random order

player1.deck.shuffle_deck()

player2.deck.shuffle_deck()

rounds = 0

# Keep playing until one player runs out of cards

while player1.card_count() > 0 and player2.card_count() > 0:

    rounds += 1

    card1 = player1.deck.draw_card()

    card2 = player2.deck.draw_card()

    print("Player 1 drew:", card1)
    print("Player 2 drew:", card2)

    # Store the cards played so the winner can collect them

    tie_cards = []

    tie_cards.append(card1)
    tie_cards.append(card2)

    # If both cards have the same value, keep drawing until the tie is broken

    was_war = False

    while card1.value == card2.value:

        was_war = True

        print("War!")
        if player1.card_count() == 0 or player2.card_count() == 0:
            break
        
        card1 = player1.deck.draw_card()
        card2 = player2.deck.draw_card()

        print("Player 1 drew:", card1)
        print("Player 2 drew:", card2)

        tie_cards.append(card1)
        tie_cards.append(card2)

    if player1.card_count() == 0 and player2.card_count() == 0:
        print("The game is a draw!")
        break

    elif player1.card_count() == 0:
        player2.collect_cards(tie_cards)
        break

    elif player2.card_count() == 0:
        player1.collect_cards(tie_cards)
        break

    elif card1.value > card2.value:
        if was_war:
            print("Player 1 wins the war!")
        else:
            print("Player 1 wins the round!")

        player1.collect_cards(tie_cards)

    else:
        if was_war:
            print("Player 2 wins the war!")
        else:
            print("Player 2 wins the round!")

        player2.collect_cards(tie_cards)

    print("Player 1 has", player1.card_count(), "cards.")
    print("Player 2 has", player2.card_count(), "cards.")

    # Check which player won the game and display the final results

if player1.card_count() == 0 and player2.card_count() == 0:
    print("The game ended in a draw!")

elif player2.card_count() == 0:
    print("Player 1 wins the game!")

elif player1.card_count() == 0:
    print("Player 2 wins the game!")

else:
    print("The game ended in a draw!")

print("Player 1 has", player1.card_count(), "cards.")
print("Player 2 has", player2.card_count(), "cards.")


print("Total rounds:", rounds)
