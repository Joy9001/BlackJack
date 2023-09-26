import os
import random

from art import logo

Rules = {
    "Objective" : "The primary goal of Blackjack is to beat the dealer's hand without going over 21",
    
    "Card Values" :  "Number cards (2-10) are worth their face value. Face cards (King, Queen, Jack) are each worth 10 points. Aces can be worth either 1 point or 11 points, depending on which value benefits the player more.",
    
    "Dealing" : "Each player and the dealer receive two cards. Players' cards are usually dealt face up, while the dealer has one card face up (the \"upcard\") and one face down (the \"hole card\")",
    
    "Blackjack" : "A Blackjack is an Ace and a 10-point card (10, Jack, Queen, King) as the initial two cards. It is the highest winning hand, usually paying 3:2",
    
    "Player Decisions" : "Players can choose to \"hit\" (take another card) or \"stand\" (keep their current hand). Players can also opt to \"double down\" (double their bet and receive one more card) or \"split\" (if they have two cards of the same rank, they can split them into separate hands)",
    
    "Dealer's Turn": "After all players have completed their actions, the dealer reveals their hole card. The dealer must hit until their hand reaches 17 or higher.",

    "Winning": "Players win by having a hand closer to 21 than the dealer without busting. If a player has a Blackjack and the dealer doesn't, the player wins automatically.",

    "Push": "If a player and the dealer have the same total (a tie), it's called a \"push\" and the player's bet is returned.",
}

if (input("Do you know the rules of BlackJack? Type 'y' if yes or 'n' if no and want to know the rules: ") == 'n'):
    for rule in Rules:
        print(rule + " : " + Rules[rule] + "\n")
else:
    print("Okay! Let's start.\n")
    
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def print_score(user, dealer):
    print("\n")
    print(f"Your Cards: {user}")
    print(f"Dealer's Cards: {dealer}")
    print(f"Your Score: {sum(user)}")
    print(f"Dealer's Score: {sum(dealer)}")
    print("\n")

def black_jack(user_score, dealer_score):
    hit = input("Do you want a hit? Type 'y' or 'n': ")
    if hit == 'y':
        user.append(random.choice(cards))
        user_score = sum(user)
        
        if 11 in user and user_score > 21:
            user.insert(user.index(11),1)
            user.remove(11)
            user_score = sum(user)

        print(f"Your Cards: {user}")
        print(f"Your Score: {user_score}")

        if user_score > 21:
            print_score(user, dealer)
            print("You Lose! BUSTED!😤\n")
            return
        elif user_score == 21:
            print_score(user, dealer)
            print("You Won! BLACKJACK!😍\n")
            return
        else:
            return black_jack(user_score, dealer_score)
    else:
        while dealer_score < 17:
            dealer.append(random.choice(cards))
            dealer_score = sum(dealer)

        if 11 in user and user_score > 21:
                user.insert(user.index(11),1)
                user.remove(11)
                user_score = sum(user)

        if 11 in dealer and dealer_score > 21:
                dealer.insert(dealer.index(11),1)
                dealer.remove(11)
                dealer_score = sum(dealer)
    
        if user_score > 21:
            print_score(user, dealer)
            print("You Lose! BUSTED!😤\n")
            return
        elif dealer_score > 21:
            print_score(user, dealer)
            print("You Won! Dealer is BUSTED!😎\n")
            return
        elif user_score == 21:
            if dealer_score == 21:
                print_score(user, dealer)
                print("DRAW! You both have same score!😶\n")
                return
            else:
                print_score(user, dealer)
                print("You Won! You have higher score!🤩\n")
                return
        elif user_score < 21:
            if user_score > dealer_score:
                print_score(user, dealer)
                print("You Won! You have higher score!🤩\n")
                return
            elif user_score < dealer_score:
                print_score(user, dealer)
                print("You Lose! You have lower score!😭\n")
                return
            else:
                print_score(user, dealer)
                print("DRAW! You both have same score!😶\n")
                return

choice  = True
while choice:
    print(logo)
    user = []
    dealer = []

    for _ in range(2):
        user.append(random.choice(cards))
        dealer.append(random.choice(cards))

    print(f"Here's Your Cards: {user[0]}, {user[1]}")
    print(f"Here's Dealer's upcard: {dealer[0]}")

    user_score = sum(user)
    dealer_score = sum(dealer)
    print(f"Your Score: {user_score}")
    
    if(user_score == 21):
        print(f"Your Cards: {user}")
        print(f"Dealer's Cards: {dealer}")
        print(f"Your Score: {user_score}")
        print(f"Dealer's Score: {dealer_score}")
        print("You Won! BLACKJACK!😍\n")
    elif dealer_score == 21:
        print(f"Your Cards: {user}")
        print(f"Dealer's Cards: {dealer}")
        print(f"Your Score: {user_score}")
        print(f"Dealer's Score: {dealer_score}")
        print("You Lose! Dealer has BLACKJACK!\n")
    else:
        black_jack(user_score, dealer_score)
    
    ch = input("Do you want to start a new game? Type 'y' or 'n': ")
    if ch == 'n':
        choice = False
    else:
        os.system('clear')
