from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter


# need to fix double tilda to not work -~-~3.
# need to fix 3l error.

def main():
    while True:
        text = input("calc > ")
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()  # try tokens = list(lexer.generate_tokens()) -> done.
        parser = Parser(tokens)
        if parser is None:
            continue
        tree = parser.parse()
        # print(tree)
        if not tree:
            continue
        interpreter = Interpreter()
        value = interpreter.visit(tree)
        if value is None:
            continue
        print(value)


def main2(text):
    text = text
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()  # try tokens = list(lexer.generate_tokens()) -> done.
    parser = Parser(tokens)
    tree = parser.parse()
    if not tree:
        return None
    interpreter = Interpreter()
    value = interpreter.visit(tree)
    return value


if __name__ == '__main__':
    main()
