def calc( a, b, operator ):
  
  if operator == "+" :
    return a + b
  elif operator == "-" :
    return a - b
  elif operator == "*" :
    return a * b
  elif operator == "/" :
    if b == 0:
      return "Not Divisible By Zero"
    return a / b
  elif operator == "%" :
    return a % b
  elif operator == "**":
    return a ** b
  else:
    return "Invalid Operator" 
  
while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    while True:
        operator = input("Select an operator (+, -, *, /, %, **): ")

        if operator in ["+", "-", "*", "/", "%", "**"]:
            break

        print("Invalid operator. Please try again.")

    result = calc(a, b, operator)
    print("Result:", result)

    choice = input("Do you want to calculate again? (yes/no): ").strip().lower()

    if choice == "no":
        break

