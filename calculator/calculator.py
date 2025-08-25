def add(a,b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b

def multiple(a,b):
    """Returns the product of a and b."""
    return a * b

def divide(a,b):
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    return a/b

print("=== Simple Calculator ===")
print("Type 'q' to quit.")

while True:
    print("\nChoose an Operation:")

    print("1.) Add")
    print("2.) Substract")
    print("3.) Multiply")
    print("4.) Divide")

    choice =input(("Which operation you want to execute out of 1,2,3,4:"
    ))

    if choice.lower() == 'q':
        print("Existing")
        break

    if choice in ('1','2','3','4'):
        num1= float(input("enter first number:"))
        num2= float(input("enter second numer:"))

        if choice =='1':
            print(f'{num1} + {num2} = {add(num1,num2)}')

        elif choice =='2':
            print(f'{num1}-{num2} = {subtract(num1,num2)}') 

        elif choice == '3':
            print(f'{num1}*{num2} = {multiple(num1,num2)}')

        elif choice == '4':
            result= divide(num1,num2)
            if result is not None:
                print(f'{num1}/{num2} = {result}')

    else:
        print("Invalid Input")