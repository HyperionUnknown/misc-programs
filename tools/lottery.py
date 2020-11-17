from random import*

money = 100
while money>1:
  shop =input("would you like to buy a lottery ticket, yes = y, no = n")
  ticket =[randint(1,99),randint(1,99),randint(1,99),randint(1,99),randint(1,99)]
  if shop == "y":
    money = money-5
    print(ticket)
    print("money =",money)
  else:
    money = money
    print("money=",money)