from tokens import Token


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
        while self.current_char is not None:
            if self.current_char.isspace():
                self.advance()
            elif self.current_char.isdigit():
                yield self.generate_number()
            elif self.current_char == '+':
                self.advance()
                yield Token(PLUS, '+')
            elif self.current_char == '-':
                self.advance()
                yield Token(MINUS, '-')
            elif self.current_char == '*':
                self.advance()
                yield Token(MUL, '*')
            elif self.current_char == '/':
                self.advance()
                yield Token(DIV, '/')
            else:
                raise Exception('Invalid character')

    def generate_number(self):
        number_str = ''
        while self.current_char is not None and self.current_char.isdigit():
            number_str += self.current_char
            self.advance()
        return Token(INTEGER, int(number_str))
