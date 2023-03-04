import random

input = input("What do you choose, rock, paper, or scissors? ")

rannum = random.randint(1, 3)

if input.lower() == "rock":
  innum = 1
elif input.lower() == "paper":
  innum = 2
elif input.lower() == "scissors" or input.lower() == "scissor":
  innum = 3
else :
  print("I don't understand")

if rannum == 1:
  ranstr = "Rock"
elif rannum == 2:
  ranstr = "Paper"
elif rannum == 3:
  ranstr = "Scissors"
print("RPS bot chose: " + ranstr)

if innum == rannum:
  print("It is a tie")
elif innum == 1 and rannum == 3:
  print("You win")
elif innum == 3 and rannum == 2:
  print("You win")
elif innum == 2 and rannum == 1:
  print("You win")
else :
  print("You lose")