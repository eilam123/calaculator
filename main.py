from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter


# need to fix double tilda to not work -~-~3.
# need to fix 3l error.


def main():
    while True:
        try:
            try:
                text = input("calc> ")
            except EOFError:
                print("EOFError")
                break

            lexer = Lexer(text)
            tokens = lexer.generate_tokens()  # try tokens = list(lexer.generate_tokens()) -> done.
            try:
                parser = Parser(tokens)
            except Exception as e:
                print(e)
                continue
            if parser is None:
                continue
            try:
                tree = parser.parse()
            # print(tree)
            except Exception as e:
                print(e)
                continue
            if not tree:
                continue
            interpreter = Interpreter()
            value = interpreter.visit(tree)
            if value is None:
                continue
            print(value)
        except KeyboardInterrupt:
            print("\nthe program was interrupted by the user.")
            break


def main2(text):
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()  # try tokens = list(lexer.generate_tokens()) -> done.
    try:
        parser = Parser(tokens)
    except Exception as e:
        print(e)
        return str(e)

    if parser is None:
        return None
    try:
        tree = parser.parse()
    # print(tree)
    except Exception as e:
        print(e)
        return str(e)
    if not tree:
        return None
    interpreter = Interpreter()
    value = interpreter.visit(tree)
    if value is None:
        return None
    return value


if __name__ == '__main__':
    main()