def add(a,b):
    return a + b

while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        result = add(num1, num2)
        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

    cont = input("Do you want to continue? (y/n): ")
    if cont.lower() != 'y':
        break

print("Calculator closed.")