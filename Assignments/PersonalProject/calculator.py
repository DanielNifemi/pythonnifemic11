def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b


a = input("Enter a number: ")
b = input("Enter a number: ")
op = input("Enter an operator: ")
print(calculator(int(a), int(b), op))
