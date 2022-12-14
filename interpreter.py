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

    # def visit_PlusNode(self, node):
    #     return Number(self.visit(node.node).value)

    def visit_PowerNode(self, node):
        return Number(self.power(self.visit(node.node_a).value, self.visit(node.node_b).value))

    def power(self, a, b):
        if b == 0 and a == 0:
            raise ZeroDivisionError("cannot divide by zero")
        return pow(a, b)
