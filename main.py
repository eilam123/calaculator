from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

while True:
    try:
        text = input("calc > ")
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()  # try tokens = list(lexer.generate_tokens()) -> done.
        parser = Parser(tokens)
        tree = parser.parse()
        print(tree)
        if not tree:
            continue
        interpreter = Interpreter()
        value = interpreter.visit(tree)
        print(value)
    except Exception as e:
        print(e)
