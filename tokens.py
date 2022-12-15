class TokenType:
    NUMBER = 0
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    POWER = 5
    MODULO = 6
    MIN = 7
    MAX = 8
    AVERAGE = 9
    FACTORIAL = 10
    TILDA = 11
    DIGITS_SUM = 12
    LPAREN = 13
    RPAREN = 14


class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __repr__(self):
        if self.type == TokenType.NUMBER:
            return "NUMBER: " + (f"{self.value}" if self.value is not None else "")
        elif self.type == TokenType.PLUS:
            return "+"
        elif self.type == TokenType.MINUS:
            return "-"
        elif self.type == TokenType.MULTIPLY:
            return "*"
        elif self.type == TokenType.DIVIDE:
            return "/"
        elif self.type == TokenType.POWER:
            return "^"
        elif self.type == TokenType.MODULO:
            return "%"
        elif self.type == TokenType.MIN:
            return "&"
        elif self.type == TokenType.MAX:
            return "$"
        elif self.type == TokenType.AVERAGE:
            return "@"
        elif self.type == TokenType.FACTORIAL:
            return "!"
        elif self.type == TokenType.TILDA:
            return "~"
        elif self.type == TokenType.DIGITS_SUM:
            return "#"
        elif self.type == TokenType.LPAREN:
            return "("
        elif self.type == TokenType.RPAREN:
            return ")"
        return "UNKNOWN TOKEN"



