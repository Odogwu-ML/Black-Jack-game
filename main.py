# Black-jack-game 
from art import logo
import random
import os

def start_message():
    to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    return to_play


def display_card_info(user_card_list, computer_card_list):
    # display user current cards and current total card value
    print(f"Your cards: {user_card_list}, current score: {sum(user_card_list)}")
    # display dealers current cards and current total card value
    print(f"Computer's first card: {computer_card_list[0]}")

while start_message() == "y":
    os.system("clear")
    print(logo)

    # list of cards
    card_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    bet_price = int(input("How much will you bet?: "))
    user_card_list = random.sample(card_list, 2)
    dealer_card_list = random.sample(card_list, 2)

    # display curren information
    display_card_info(user_card_list, dealer_card_list)
    

    to_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    while to_continue == "y":
        # get new card at random from the list of cards
        new_card = random.choice(card_list)
        if new_card == 11 and sum(user_card_list) < 21:
            ace_value = int(input("Select ace value (1/11): "))
            new_card = ace_value
        # Add the new card to the users list of cards
        user_card_list.append(new_card)
        display_card_info(user_card_list, dealer_card_list)
        

        if sum(user_card_list) > 21:
            print(f"your final hand: {user_card_list}, final score: {sum(user_card_list)}")
            print(f"Computers final hand: {dealer_card_list}, final_score: {sum(dealer_card_list)}")
            print("You went over. You lose")
        elif user_card_list == 21:
            print(f"your final hand: {user_card_list}, final score: {sum(user_card_list)}")
            print(f"Computers final hand: {dealer_card_list}, final_score: {sum(dealer_card_list)}")
            print("You win!")
        else:
            to_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()


    user_total_card = sum(user_card_list)
    dealers_total_card = sum(dealer_card_list)

    if dealer_card_list < 17:
        additonal_card = random.choice(card_list)
        dealer_card_list.append(additonal_card)

    if user_total_card > dealers_total_card:
            print(f"your final hand: {user_card_list}, final score: {user_total_card}")
            print(f"Computers final hand: {dealer_card_list}, final_score: {dealers_total_card}")
            print("You win!")
    elif dealers_total_card > user_total_card:
            print(f"your final hand: {user_card_list}, final score: {user_total_card}")
            print(f"Computers final hand: {dealer_card_list}, final_score: {dealers_total_card}")
            print("Computer wins!")



