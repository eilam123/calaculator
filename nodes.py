class NumberNode:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'({self.value})'


class AddNode:
    def __init__(self, node_a, node_b):
        self.node_a = node_a
        self.node_b = node_b

    def __repr__(self):
        return f"({self.node_a}+{self.node_b})"


class SubtractNode:
    def __init__(self, node_a, node_b):
        self.node_a = node_a
        self.node_b = node_b

    def __repr__(self):
        return f"({self.node_a}-{self.node_b})"


class MultiplyNode:
    def __init__(self, node_a, node_b):
        self.node_a = node_a
        self.node_b = node_b

    def __repr__(self):
        return f"({self.node_a}*{self.node_b})"


class DivideNode:
    def __init__(self, node_a, node_b):
        self.node_a = node_a
        self.node_b = node_b

    def __repr__(self):
        return f"({self.node_a}/{self.node_b})"


class MinusNode:
    def __init__(self, node):
        self.node = node

    def __repr__(self):
        return f"(-{self.node})"


# @dataclass
# class PlusNode:
#     node: any
#
#     def __repr__(self):
#         return f"(+{self.node})"


class PowerNode:
    def __init__(self, node_a, node_b):
        self.node_a = node_a
        self.node_b = node_b

    def __repr__(self):
        return f"({self.node_a}^{self.node_b})"


class ModuloNode:
    def __init__(self, node_a, node_b):
        self.node_a = node_a
        self.node_b = node_b

    def __repr__(self):
        return f"({self.node_a}%{self.node_b})"


class MaxNode:
    def __init__(self, node_a, node_b):
        self.node_a = node_a
        self.node_b = node_b

    def __repr__(self):
        return f"(({self.node_a}${self.node_b}))"


class MinNode:
    def __init__(self, node_a, node_b):
        self.node_a = node_a
        self.node_b = node_b

    def __repr__(self):
        return f"(({self.node_a}&{self.node_b}))"


class AverageNode:

    def __init__(self, node_a, node_b):
        self.node_a = node_a
        self.node_b = node_b

    def __repr__(self):
        return f"({self.node_a}@{self.node_b})"


class FactorialNode:
    def __init__(self, node):
        self.node = node

    def __repr__(self):
        return f"({self.node}!)"


class TildaNode:
    def __init__(self, node):
        self.node = node

    def __repr__(self):
        return f"(~{self.node})"


class DigitsSumNode:
    def __init__(self, node):
        self.node = node

    def __repr__(self):
        return f"({self.node}#)"
