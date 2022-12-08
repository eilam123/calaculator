from tokens import Token, TokenType

WHITESPACE = ' \n\t'
DIGITS = '0123456789'


class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char != None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char in DIGITS:  # delete self.current_char == '.' or because i dont want to allow number like .123 (start with .) -> done.
                yield self.generate_number()
            elif self.current_char == '+':
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == '-':
                self.advance()
                yield Token(TokenType.MINUS)
            # elif self.current_char == '-' and next(self.text) not in DIGITS:
            #     self.advance()
            #     yield Token(TokenType.MINUS)
            # elif self.current_char == '-' and next(self.text) in DIGITS:
            #     yield self.generate_number()
            # elif self.current_char == '-' and next(self.text) in DIGITS:  # if '-' is followed by digit -> done.
            #     self.advance()
            #     yield Token(TokenType.UNARY_MINUS)
            elif self.current_char == '*':
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == '/':
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.RPAREN)
            elif self.current_char == '^':
                self.advance()
                yield Token(TokenType.POWER)
            elif self.current_char == '.':
                raise Exception("Number can't start with '.'")
            else:
                raise Exception(f"Illegal character '{self.current_char}'")

    def generate_number(self):
        decimal_point_count = 0
        number_str = self.current_char
        self.advance()

        while self.current_char != None and (self.current_char == '.' or self.current_char in DIGITS):
            if self.current_char == '.':
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break

            number_str += self.current_char
            self.advance()

        if number_str[0] == '0' and number_str[1] != '.':
            raise Exception("Number can't start with '0' if there is no '.' after it")
        if number_str.endswith('.'):  # if number end with '.' add raise exception -> done.
            raise Exception("Number can't end with '.'")

        return Token(TokenType.NUMBER, float(number_str))
