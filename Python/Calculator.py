# Taking 2 numbers are input
number1= int(input("Enter number 1: "))
number2= int(input("Enter number 2: "))
# Taking operator as input
operator= input("Enter the operator: [+, -, *, /]:")
# let's do the calculation
if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)