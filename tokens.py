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
        return self.type.name + (f":{self.value}" if self.value is not None else "")
