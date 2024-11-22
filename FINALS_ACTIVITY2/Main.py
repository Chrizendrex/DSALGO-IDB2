from LinkedStack import LinkedStack
from PositionalList import PositionalList
s= LinkedStack
p = PositionalList

def precedence(op):
    """Return the precedence of the operator."""
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0

def preprocess_expression(expression):
    """Add spaces around operators and parentheses for proper tokenization."""
    operators = set('+-*/^()')
    result = []
    for char in expression:
        if char in operators:
            result.append(f' {char} ')
        else:
            result.append(char)
    return ''.join(result).split()

def infix_to_postfix(expression):
    """Convert an infix expression to postfix notation."""
    stack = []
    output = []

    for char in expression:
        if char.isdigit():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return " ".join(output)

def main():
    expression = input("Enter an infix expression : ").strip()
    try:
        tokens = preprocess_expression(expression)
        postfix = infix_to_postfix(tokens)
        print("Postfix:", postfix)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

def insertion_sort_ascending(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key

def insertion_sort_descending(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] < key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key


input_string = input("Enter a list of numbers separated by spaces: ")
num = list(map(int, input_string.split()))

positional_list = num.copy()

print("\nOriginal Array:", num)

insertion_sort_ascending(positional_list)
print("Ascending Order:", positional_list)

insertion_sort_descending(positional_list)
print("Descending Order:", positional_list)