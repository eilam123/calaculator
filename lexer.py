from tokens import Token, TokenType

WHITESPACE = ' \n\t'
DIGITS = '0123456789'


# add comments to the code
class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        """Advance the `self.current_char` pointer and set the `self.current_char` variable."""
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        """Lexical analyzer (also known as scanner or tokenizer) this method breaks a sentence apart into tokens. One token at a time."""
        while self.current_char is not None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char.isdigit():  # delete self.current_char == '.' or because i dont want to allow number like .123 (start with .) -> done.
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
            elif self.current_char == '%':
                self.advance()
                yield Token(TokenType.MODULO)
            elif self.current_char == '$':
                self.advance()
                yield Token(TokenType.MAX)
            elif self.current_char == '&':
                self.advance()
                yield Token(TokenType.MIN)
            elif self.current_char == '@':
                self.advance()
                yield Token(TokenType.AVERAGE)
            elif self.current_char == '!':
                self.advance()
                yield Token(TokenType.FACTORIAL)
            elif self.current_char == '~':
                self.advance()
                yield Token(TokenType.TILDA)
            elif self.current_char == '#':
                self.advance()
                yield Token(TokenType.DIGITS_SUM)
            elif self.current_char == '.':
                raise Exception("Number can't start with '.'")
            else:
                raise ValueError(f"Illegal character '{self.current_char}'")

    def generate_number(self):
        """this method takes the current character and keeps adding it to the number until it sees a non-digit character.
            It then converts the string of digits into an integer and returns a NUMBER token.
        """
        decimal_point_count = 0
        number_str = self.current_char
        self.advance()

        while self.current_char is not None and (self.current_char == '.' or self.current_char in DIGITS):
            if self.current_char == '.':
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break

            number_str += self.current_char
            self.advance()
        if len(number_str) > 1:
            if number_str[0] == '0' and number_str[1] != '.':
                raise Exception("Number can't start with '0' if there is no '.' after it")
        if number_str.endswith('.'):  # if number end with '.' add raise exception -> done.
            raise Exception("Number can't end with '.'")

        return Token(TokenType.NUMBER, float(number_str))
