# Simple 4 function calculator with two inputs
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print("Select one")
print("-------------")
print("Add")
print("Subtract")
print("Multiply")
print("Divide")
print(" ")

while True:
    choice = input("Enter you selection: ")
    if choice in("add", "subtract", "multiply", "divide"):
        num1 = float(input("Enter your number: "))
        num2 = float(input("Enter your number: "))
        if choice == "add":
            print(num1, "+", num2, "=", add(num1,num2))
        elif choice == "subtract":
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == "multiply":
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == "divide":
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid")