import random

choices = {
    "s": "snake",
    "w": "water",
    "g": "gun",
}

winning_pairs = {
    ("snake", "water"),
    ("water", "gun"),
    ("gun", "snake"),
}

print("Snake Water Gun Game")
print("Choose one: s for snake, w for water, g for gun")

user_key = input("Enter your choice: ").strip().lower()

if user_key not in choices:
    print("Invalid choice. Please run the game again and choose s, w, or g.")
else:
    user_choice = choices[user_key]
    computer_choice = random.choice(list(choices.values()))

    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {user_choice}")

    if user_choice == computer_choice:
        print("Match draw!")
    elif (user_choice, computer_choice) in winning_pairs:
        print(f"{user_choice.title()} beats {computer_choice}.")
        print("You win!")
    else:
        print(f"{computer_choice.title()} beats {user_choice}.")
        print("You lose!")
