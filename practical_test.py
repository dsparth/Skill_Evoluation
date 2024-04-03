# Taking postfix expression input from the user
postfix_expression = input("Enter postfix expression: ")

def evaluate_postfix(expression):
    stack = []
    operators = set(['+', '-', '*', '/'])

    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        elif char in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                stack.append(operand1 // operand2)  # Use integer division for simplicity

    return stack.pop()

# Evaluating the postfix expression
result = evaluate_postfix(postfix_expression)
print("Result of evaluating postfix expression:", result)
