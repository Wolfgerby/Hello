def start_game():
    print("Welcome to the Adventure Game!")
    choice = input("Do you want to go into the forest or the cave? (forest/cave) ")
    if choice == "forest":
        forest()
    elif choice == "cave":
        cave()
    else:
        print("Invalid choice, try again.")
        start_game()

def forest():
    print("You are in a dark forest. You see a path ahead.")
    choice = input("Do you want to follow the path or return? (path/return) ")
    if choice == "path":
        print("You found a treasure! You win!")
    elif choice == "return":
        start_game()
    else:
        print("Invalid choice, try again.")
        forest()

def cave():
    print("You are in a spooky cave. You hear a noise.")
    choice = input("Do you want to investigate or leave? (investigate/leave) ")
    if choice == "investigate":
        print("A monster appears! You lose!")
    elif choice == "leave":
        start_game()
    else:
        print("Invalid choice, try again.")
        cave()

