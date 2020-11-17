
num1 = input("first number")
num2 = input("second number")
process = input("type in *,/,+,-")
num1 = int(num1)
num2 = int(num2)
if process == "*":
  print(num1*num2)
elif process == "+":
  print(num1+num2)
elif process == "/":
  print(num1/num2)
elif process == "-":
  print(num1-num2)
