from dataclasses import dataclass


@dataclass
class NumberNode:
    value: any

    def __repr__(self):
        return f"{self.value}"


@dataclass
class AddNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}+{self.node_b})"


@dataclass
class SubtractNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}-{self.node_b})"


@dataclass
class MultiplyNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}*{self.node_b})"


@dataclass
class DivideNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}/{self.node_b})"


@dataclass
class MinusNode:
    node: any

    def __repr__(self):
        return f"(-{self.node})"


# @dataclass
# class PlusNode:
#     node: any
#
#     def __repr__(self):
#         return f"(+{self.node})"


@dataclass
class PowerNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}^{self.node_b})"


@dataclass
class ModuloNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}%{self.node_b})"


@dataclass
class MaxNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}${self.node_b})"  # return f"max({self.node_a},{self.node_b})"


@dataclass
class MinNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}&{self.node_b})"  # return f"min({self.node_a},{self.node_b})"


@dataclass
class AverageNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}@{self.node_b})"  # return f"({self.node_a}+{self.node_b})/2"


@dataclass
class FactorialNode:
    node: any

    def __repr__(self):
        return f"({self.node}!)"


@dataclass
class TildaNode:
    node: any

    def __repr__(self):
        return f"~{self.node}"


@dataclass
class DigitsSumNode:
    node: any

    def __repr__(self):
        return f"{self.node}#"
