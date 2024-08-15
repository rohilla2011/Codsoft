import random
options = ["Rock", "Paper", "Scissors"]
user_choice = input("Choose Rock, Paper, or Scissors: ")
comp_choice = random.choice(options) 
print("You chose: ", user_choice)
print("Computer chose: ", comp_choice)
if user_choice == comp_choice:

    print("It's a tie!")
elif user_choice == "Rock" and comp_choice == "Scissors":

    print("You win!")
elif user_choice == "Paper" and comp_choice == "Rock":

    print("You win!")
elif user_choice == "Scissors" and comp_choice == "Paper":

    print("You win!")
else:

    print("Computer wins!")

