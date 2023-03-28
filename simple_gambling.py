import random


def roll():
    result = random.randint(1, 6)
    print(f"\033[1mYou rolled a {result}!\033[0m\n")


def flip():
    result = random.choice(["heads", "tails"])
    print(f"\033[1mThe coin landed on {result}!\033[0m\n")

def betflip():
    bet = input("How much would you like to bet? ")
    bet = float(bet)

    if bet <= 0:
        print("\033[91mInvalid bet. Please enter a positive number.\033[0m\n")
        return

    if bet > 10:
        print("\033[91mSorry, the maximum bet allowed is $10.00.\033[0m\n")
        return

    print("You flipped a coin! If it lands on your chosen side, you win double your bet.")
    chosen_side = input("Choose 'heads' or 'tails': ").lower()

    if chosen_side not in ["heads", "tails"]:
        print("\033[91mInvalid choice. Please choose 'heads' or 'tails'.\033[0m\n")
        return

    result = random.choice(["heads", "tails"])

    if result == chosen_side:
        winnings = bet * 2
        print(f"\033[92mThe coin landed on {result}! You win ${winnings:.2f}!\033[0m\n")
    else:
        print(f"\033[91mThe coin landed on {result}. You lost ${bet:.2f}.\033[0m\n")


def betroll():
    bet = input("How much would you like to bet? ")
    bet = float(bet)

    if bet <= 0:
        print("\033[91mInvalid bet. Please enter a positive number.\033[0m\n")
        return

    if bet > 10:
        print("\033[91mSorry, the maximum bet allowed is $10.00.\033[0m\n")
        return

    print("You are rolling a die! If it lands on your chosen number, you win double your bet.")
    chosen_number = input("Choose a number between 1 and 6: ")
    chosen_number = int(chosen_number)

    if chosen_number < 1 or chosen_number > 6:
        print("\033[91mInvalid choice. Please choose a number between 1 and 6.\033[0m\n")
        return

    result = random.randint(1, 6)

    if result == chosen_number:
        winnings = bet * 2
        print(f"\033[92mYou rolled a {result}! You win ${winnings:.2f}!\033[0m\n")
    else:
        print(f"\033[91mYou rolled a {result}. You lost ${bet:.2f}.\033[0m\n")