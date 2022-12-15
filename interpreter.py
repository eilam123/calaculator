from nodes import *
from values import Number


class Interpreter:
    def __init__(self):
        pass

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)

    def visit_NumberNode(self, node):
        return Number(node.value)

    def visit_AddNode(self, node):
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

    def visit_SubtractNode(self, node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    def visit_MultiplyNode(self, node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

    def visit_DivideNode(self, node):
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except:
            raise ZeroDivisionError("cannot divide by zero")

    def visit_MinusNode(self, node):
        return Number(-self.visit(node.node).value)

    def visit_ModuloNode(self, node):
        try:
            return Number(self.visit(node.node_a).value % self.visit(node.node_b).value)
        except:
            raise ZeroDivisionError("cannot divide by zero")

    def visit_MinNode(self, node):
        return Number(min(self.visit(node.node_a).value, self.visit(node.node_b).value))

    def visit_MaxNode(self, node):
        return Number(max(self.visit(node.node_a).value, self.visit(node.node_b).value))

    def visit_AverageNode(self, node):
        return Number((self.visit(node.node_a).value + self.visit(node.node_b).value) / 2)

    def visit_FactorialNode(self, node):
        return Number(self.factorial(self.visit(node.node).value))

    def visit_TildaNode(self, node):
        return Number(self.visit(node.node).value*-1)

    def visit_DigitsSumNode(self, node):
        return Number(self.digits_sum(self.visit(node.node).value))

    # def visit_PlusNode(self, node):
    #     return Number(self.visit(node.node).value)

    def visit_PowerNode(self, node):
        return Number(self.power(self.visit(node.node_a).value, self.visit(node.node_b).value))

    def power(self, a, b):
        if b == 0 and a == 0:
            raise ZeroDivisionError("cannot divide by zero")
        if a < 0 and b % 1 != 0:
            raise ValueError("cannot raise negative number to a non-integer power")
        return pow(a, b)

    def factorial(self, n):
        if n < 0:
            raise ValueError("factorial is not defined for negative numbers")
        if n == 0:
            return 1
        return n * self.factorial(n - 1)

    def digits_sum(self, n):
        if n < 0:
            n = -n
        return sum(float(i) for i in str(n) if i.isdigit())
