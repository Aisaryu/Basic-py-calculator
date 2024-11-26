def addition(x,y):
  return round(x + y, 2)

def subtraction(x,y):
  return round(x - y, 2)

def multiplication(x,y):
  return round(x * y, 2)

def division(x,y):
  try:
    return x / y

  except ZeroDivisionError:
    return "Error: Cannot divide by 0"

while True:
  print("A. Addition, B. Subtraction, C. Multiplication, D. Division")

  userSelect = input("Select an operation: ").upper()

  if userSelect not in ("A", "B", "C", "D"):
    print("Error: Invalid option")
    break

  num1 = float(input("Enter the 1st number: "))
  num2 = float(input("Enter the 2nd number: "))

  options = {
    "A":addition(num1, num2),
    "B":subtraction(num1, num2),
    "C":multiplication(num1, num2),
    "D":division(num1,num2)
  }

  if userSelect in options:
    if userSelect == "A":
      print("Addition: ", options[userSelect])

    elif userSelect == "B":
      print("Subtraction: ", options[userSelect])

    elif userSelect == "C":
      print("Multiplacation: ", options[userSelect])

    elif userSelect == "D":
      print("Division: ", options[userSelect])

  else:
    print("Error: Invalid option")

  print("\n")
  