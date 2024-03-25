
# Ask for playerOne's name and store it in the variable "player_one_name"
player_one_name = input("What is your name, playerOne??\n")
# Define a function for the first question
def question_one():
    # Print player one's name and tell them they must answer the first riddle to move onto the next question
    print("Answer this, " + player_one_name + ". Get it right and you will be one step closer to freedom.")
    # Print the first riddle
    print("What type of room has no windows or doors?")
    # Get the player's answer and convert it to lowercase
    answer = input().strip().lower()
    # print(answer)
    # If the answer is correct, proceed to the next question (if portion of the if else statement)
    # answer = input().strip().lower()
    if answer == "a mushroom":
        print("Correct...")
        print("Let's move on. NEXT QUESTION!!")
        question_two()
        # If the answer is incorrect, let the user know and ask the question again (else portion of if else statement)
    else:
        print("Wrong answer! Quick! Try again before I change my mind >:)")
        question_one()
# Define a function for the second question
def question_two():
    # Print the second riddle
    print("What can you catch but can't throw?")
    # Get the player's answer and convert it to lowercase
    answer = input().strip().lower()
    # If the answer is correct, proceed to the next question (if portion of the if else statement)
    if answer == "the flu":
        print("Right! Moving on.")
        question_three()
    # If the answer is incorrect, let the user know and ask the question again (else portion of if else statement)
    else:
        print("Wrong!! I'll give you another chance.")
        question_two()
# Define a function for the third question
def question_three():
    # Print the third riddle
    print("What grows when it eats but dies when it drinks?")
    # Get the player's answer and convert it to lowercase

    # If the answer is correct, exit the game (if portion of the if else statement)
    answer = input()
    if answer == "fire":
        print("Well done," + player_one_name + " you did it!")
        exit_game()
    # If the answer is incorrect, ask the question again (else portion of if else statement)
    else:
        print("Nuh Uh! Try one last time")
        question_three()
# Define a function to end the game
def exit_game():
    # Print a congratulations message with the player's name
    print("You made it " + player_one_name + " Good job. Enjoy your freedom and don't enter any dark tunnels again...")

# If this script is the main script (not imported from another script), start the game
if __name__ == "__main__":
    question_one()
