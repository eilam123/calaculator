from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter


def main():
    while True:
        text = input("calc > ")
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()  # try tokens = list(lexer.generate_tokens()) -> done.
        parser = Parser(tokens)
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
    try:
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
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
