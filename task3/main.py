from Stack import Stack
from Operator import Operator

ops = {
        '*': Operator(2, 1, lambda a, b: [a * b]),
        '/': Operator(2, 1, lambda a, b: [a // b]),
        '+': Operator(2, 1, lambda a, b: [a + b]),
        '-': Operator(2, 1, lambda a, b: [a - b]),
    }


def calculate(input_expression):
    input_expression = input_expression.split()
    stack = Stack()
    for n in input_expression:
        try:
            stack.append(int(n))
        except ValueError:
            try:
                op = ops[n]
                op(stack)
            except KeyError:
                raise ValueError("unknown operator {}".format(n))
    return stack


if __name__ == '__main__':
    expression = input()
    print(int(calculate(expression)[0]))
