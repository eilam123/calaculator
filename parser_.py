from tokens import TokenType, Token
from nodes import *


class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()
        self.flag = True

    def raise_error(self):
        try:
            token = self.current_token
            self.advance()
            raise Exception(f"this character is not allowed in this place: {token}")
        except Exception as e:
            print(e)

    def advance(self):
        """Advance the `current_token` to the next token on the token list of tokens."""
        try:
            self.current_token = next(self.tokens)

        except StopIteration:
            self.current_token = None
        except ValueError as e:
            # print(e)
            # self.current_token = None
            raise
        except Exception as e:
            # self.current_token = None
            # print(e)
            raise

    def parse(self):
        if self.current_token is None:
            return None

        result = self.expr()

        if self.current_token is not None:
            self.raise_error()

        return result

    # all the functions below are parts of the recursive descent parser algorithm.
    def expr(self):
        result = self.term1()

        while self.current_token is not None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.current_token.type == TokenType.PLUS:
                self.advance()
                result = AddNode(result, self.term1())
            elif self.current_token.type == TokenType.MINUS:
                self.advance()
                result = SubtractNode(result, self.term1())

        return result

    def term1(self):
        result = self.term2()

        while self.current_token is not None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            if self.current_token.type == TokenType.MULTIPLY:
                self.advance()
                result = MultiplyNode(result, self.term2())
            elif self.current_token.type == TokenType.DIVIDE:
                self.advance()
                result = DivideNode(result, self.term2())

        return result

    def term2(self):
        result = self.term3()

        while self.current_token is not None and self.current_token.type == TokenType.POWER:
            if self.current_token.type == TokenType.POWER:
                self.advance()
                result = PowerNode(result, self.term3())

        return result

    def term3(self):
        result = self.term4()

        while self.current_token is not None and self.current_token.type == TokenType.MODULO:
            if self.current_token.type == TokenType.MODULO:
                self.advance()
                result = ModuloNode(result, self.term4())
        return result

    def term4(self):
        result = self.term5()

        while self.current_token is not None and self.current_token.type in (TokenType.MAX, TokenType.MIN, TokenType.AVERAGE):
            if self.current_token.type == TokenType.MAX:
                self.advance()
                result = MaxNode(result, self.term5())
            elif self.current_token.type == TokenType.MIN:
                self.advance()
                result = MinNode(result, self.term5())
            elif self.current_token.type == TokenType.AVERAGE:
                self.advance()
                result = AverageNode(result, self.term5())
        return result

    def term5(self):
        result = self.factor()
        while self.current_token is not None and self.current_token.type in (TokenType.FACTORIAL, TokenType.DIGITS_SUM):
            if self.current_token.type == TokenType.FACTORIAL:
                self.advance()
                result = FactorialNode(result)
            elif self.current_token.type == TokenType.DIGITS_SUM:
                self.advance()
                result = DigitsSumNode(result)
        return result

    def factor(self):
        token = self.current_token
        try:
            if token.type == TokenType.LPAREN:
                self.advance()
                result = self.expr()

                if self.current_token.type != TokenType.RPAREN:
                    self.raise_error()

                self.advance()
                return result

            elif token.type == TokenType.NUMBER:
                self.advance()
                return NumberNode(token.value)

            elif token.type == TokenType.MINUS:
                self.advance()
                return MinusNode(self.factor())

            elif token.type == TokenType.TILDA and self.flag:
                self.flag = False
                self.advance()
                token = self.current_token
                if token.type == TokenType.MINUS:
                    return MinusNode(self.factor())
                elif token.type == TokenType.NUMBER:
                    self.advance()
                    self.flag = True
                    return NumberNode(-token.value)
                elif token.type == TokenType.LPAREN:
                    self.advance()
                    self.flag = True
                    result = self.expr()
                    if self.current_token.type != TokenType.RPAREN:
                        self.raise_error()
                    self.advance()
                    return MinusNode(result)

            # elif token.type == TokenType.PLUS:
            #     self.advance()
            #     return PlusNode(self.factor())

            self.raise_error()
        except AttributeError as e:
            print(e)
