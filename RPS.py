#RPS.py
#Name: Blake Green  
#Date: 9/8/25
#Assignment: RPS
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.
  play_again = "y"

  while play_again == "y":
    number = random.randint(1, 3)
    if number == 1:
      computer = "R"
    elif number == 2:
      computer = "P"
    else:
      computer = "S"
    user = input("Enter R for Rock, P for Paper, or S for Scissors: ")

    if user == computer:
      print("It's a tie! Computer chose", computer)
      ties = ties + 1
    elif user == "R" and computer == "S":
      print("You win! Computer chose", computer)
      wins = wins + 1
    elif user == "P" and computer == "R":
      print("You win! Computer chose", computer)
      wins = wins + 1
    elif user == "S" and computer == "P":
      print("You win! Computer chose", computer)
      wins = wins + 1
    else:
      print("You lose! Computer chose", computer)
      losses = losses + 1

    play_again = input("would you like to play again? (y/n): ")

    print("Wins \t Ties \t Losses")
    print("---- \t ---- \t ------")
    print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
