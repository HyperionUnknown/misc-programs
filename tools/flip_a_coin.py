from random import randint

fac = input("would you like to flip a coin, if yes type a lower case y, if no type a lower case n")
if fac == "y":
  hot = randint(1,2)
  if hot == 2:
    print("you got heads")
  else:
    print("you got tails")
else:
  quit()
