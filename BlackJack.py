from art import logo, card
import random
import os


def clear_terminal():
    if os.name == "nt":
        os.system("cls")


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user, computer):
    if user == computer:
        return "Draw"
    elif computer == 0:
        return "Lose, opponent has Blackjack"
    elif user == 0:
        return "Win with a Blackjack"
    elif user > 21:
        return "You went over. You lose"
    elif computer > 21:
        return "Opponent went over. You win"
    elif user > computer:
        return "You win"
    else:
        return "You lose"


def play_game():
    user_list = []
    computer_list = []
    is_game_over = False

    for _ in range(2):
        user_list.append(deal_card())
        computer_list.append(deal_card())

    print(logo)
    print(card)

    while not is_game_over:

        user_score = calculate_score(user_list)
        computer_score = calculate_score(computer_list)
        print(f"Your cards: {user_list}, current score: {user_score}")
        print(f"Computer's first card: {computer_list[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if another_card == "y":
                user_list.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_list.append(deal_card())
        computer_score = calculate_score(computer_list)

    print(f"Your final hand: {user_list}, final score: {user_score}")
    print(
        f"Computer's final hand: {computer_list}, final score: {computer_score}")
    print(compare(user=user_score, computer=computer_score))


while input("Do you want to play a game of Blackjack? type 'y' or 'n': ") == 'y':
    clear_terminal()
    play_game()
