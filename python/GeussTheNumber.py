import random

Range1: int = int(input("Smallest possible number: "))
Range2: int = int(input("Largest possible number: "))

rannum: int = random.randint(Range1, Range2)

con: bool = "True"
while con == "True":
  Ans: int = int(input("What is your geuss? "))
  if Ans == rannum:
    print("You geussed the number!")
    con = "False"
  else:
    q: str = input("Do you want continue? ")
    if q.lower() == "yes":
      print("Okay i will continue")
    elif q.lower() == "no":
      print("Ending the program")
      print("The answer was", rannum)
      con = "False"
    else:
      print("I assume you said yes, i will continue")
      