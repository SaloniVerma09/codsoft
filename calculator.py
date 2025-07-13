def get_number(prompt):
    while True:
        entry = input(prompt)
        try:
            return float(entry)
        except ValueError:
            print("That's not a valid number. Please try again.")

def get_operation():
    ops = ['+', '-', '*', '/']
    while True:
        op = input("Choose an operation (+, -, *, /): ").strip()
        if op in ops:
            return op
        print("Invalid operation. Please pick one of +, -, *, or /.")

def calculate(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            return None  # We'll handle this outside
        return num1 / num2

def main():
    while True:
        a = get_number("Enter the first number: ")
        b = get_number("Enter the second number: ")
        operator = get_operation()
        result = calculate(a, b, operator)
        if result is None:
            print("Division by zero isn’t allowed. Let's start over.\n")
            continue

        # Display result
        print(f"\n {a} {operator} {b} = {result}\n")
        print("THE OUTPUT = ",result)

        # Ask to continue
        again = input("Do you want to calculate again? (yes/no): ").strip().lower()
        if again not in ('yes', 'y'):
            print("Thanks for using the calculator.")
            break

if __name__ == "__main__":
    main()
