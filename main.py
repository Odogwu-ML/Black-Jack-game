# Black-jack-game 
from art import logo
import random
import os

CARD_LIST = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def start_message():
    return input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
     

def display_card_info(user_card_list, computer_card_list):
    # display user current cards and current total card value
    print(f"Your cards: {user_card_list}, current score: {sum(user_card_list)}")
    # display dealers current cards and current total card value
    print(f"Computer's first card: {computer_card_list[0]}")

def display_final_hands(user_hand, computer_hand):
    print(f"Your final hand: {user_hand}, final score: {sum(user_hand)}")
    print(f"Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}")

def ace_card(card, users_hand):
     if card == 11 and sum(users_hand) < 21:
        ace_value = int(input("Select ace value (1/11): "))
        return ace_value

def Black_jack():

    while start_message() == "y":
        os.system("clear")
        print(logo)

        # list of cards
        bet = int(input("How much will you bet?: "))
        users_hand = random.sample(CARD_LIST, 2)
        dealers_hand = random.sample(CARD_LIST, 2)

        # display curren information
        display_card_info(users_hand, dealers_hand)
        

        to_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        while to_continue == "y":
            # get new card at random from the list of cards
            new_card = random.choice(CARD_LIST)
            new_card = ace_card(new_card)

            # Add the new card to the users list of cards
            users_hand.append(new_card)

            display_card_info(users_hand, dealers_hand)
            

            if sum(users_hand) > 21:
                display_final_hands(users_hand, dealers_hand)
                return "You went over. You lose"
            elif sum(users_hand) == 21:
                display_final_hands(users_hand, dealers_hand)
                return "You win!"
            else:
                to_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()


        user_total_card_value = sum(users_hand)
        dealers_total_card_value = sum(dealers_hand)

        if dealers_total_card_value < 17:
            additonal_dealer_card = random.choice(CARD_LIST)
            dealers_hand.append(additonal_dealer_card)

        if user_total_card_value > dealers_total_card_value:
                display_final_hands(users_hand, dealers_hand)
                return "You win!"
        elif dealers_total_card_value > user_total_card_value:
                display_final_hands(users_hand, dealers_hand)
                return "Computer wins!"
        else:
             return "It's a tie"
    


result = Black_jack()
print(result)