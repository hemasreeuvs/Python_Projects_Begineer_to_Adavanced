 def display_choice(choice):
    """
    Displays an ASCII art diagram for Rock, Paper, or Scissors.
    
    Args:
        choice (str): The user's choice ('rock', 'paper', or 'scissors').
    """
    rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """

    paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    """

    scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """

    # Use a dictionary to map the choice to the correct diagram
    diagrams = {
        'rock': rock,
        'paper': paper,
        'scissors': scissors
    }
    # Check if the choice is valid and print the corresponding diagram
    if choice in diagrams:
        print(diagrams[choice])
    else:
        print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")

# --- Example Usage ---

print("Here is the Rock diagram:")
display_choice('rock')
print("\nHere is the Paper diagram:")
display_choice('paper')
print("\nHere is the Scissors diagram:")
display_choice('scissors')

# now the real game starts
user_choice = input("What do you choose? Type 0 for Rock , 1 for paper and 2 for scissors")

computer_choice = random.radint(a:0 , b:2)
print (f"computer chose {computer_choice}")

if user_choice >= 3 and computer_choice <0:
   print("you typed an invalid number. You lose!")
elif computer_choice > user_choice :
   print("you loose")
elif computer_choice == user_choice:
   print ("Its a draw")
elif computer_choice == 0 and user_choice == 2 :
   print("you loose")
elif user_choice > computer_choice:
   print("You win!")
elif user_choice >= 3 or user_choice < 0:
   print("You typed an invalid number. You lose")



   
   