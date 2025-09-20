import random

user_score = 0
comp_score = 0
choices = ["stone", "paper", "scissor"]

while True:
    user = input("ENTER PLAY OR QUIT = ").lower()
    if user == "quit":
        print(f"GAME OVER 🎮 = your = {user_score}, comp = {comp_score}")
        break
    elif user != "play":
        print("Invalid input! Type 'play' or 'quit'.")
        continue

    user_move = input("ENTER YOUR MOVE (stone/paper/scissor) = ").lower()
    if user_move not in choices:
        print("Invalid move! Try again.")
        continue

    comp_move = random.choice(choices)
    print(f"Computer chose: {comp_move}")

    if user_move == comp_move:
        print("DRAW, PLAY AGAIN OR QUIT")
    elif (user_move == "stone" and comp_move == "scissor") or \
         (user_move == "paper" and comp_move == "stone") or \
         (user_move == "scissor" and comp_move == "paper"):
        print("You win! 🎉")
        user_score += 1
    else:
        print("Computer wins! 🎉")
        comp_score += 1
