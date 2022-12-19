# Import the pytest module
import pytest
from main import main2
from values import Number
from lexer import Lexer
from parser_ import Parser


# Simple syntax errors
def test_ilegal_char():
    string = "5l"
    assert main2(string) == "Illegal character 'l'"


def test_none_sense():
    string = "y2rhudn01203rhfi2ba!@#"
    assert main2(string) == "Illegal character 'y'"


# ptytest raises not working as expected
# def test_ilegal_syntax():
#     text = "3^*2"
#     with pytest.raises(Exception):
#         lexer = Lexer(text)
#         tokens = lexer.generate_tokens()
#         parser = Parser(tokens)
#         parser.parse()


def test_addition_operator():
    string = "1+2"
    assert main2(string) == Number(3)


def test_subtraction_operator():
    string = "7-3"
    assert main2(string) == Number(4)


def test_multiplication_operator():
    string = "3*4"
    assert main2(string) == Number(12)


def test_division_operator():
    string = "15/4"
    assert main2(string) == Number(3.75)


def test_power_operator():
    string = "-3^3"
    assert main2(string) == Number(-27)


def test_mod_operator():
    string = "6%3"
    assert main2(string) == Number(0)


def test_max_operator():
    string = "4$9"
    assert main2(string) == Number(9)


def test_min_operator():
    string = "6&1"
    assert main2(string) == Number(1)


def test_avg_operator():
    string = "5@15"
    assert main2(string) == Number(10)


def test_tilda_operator():
    string = "~--3"
    assert main2(string) == Number(-3)


def test_factorial_operator():
    string = "6!"
    assert main2(string) == Number(720)


def test_sum_digits_operator():
    string = "15364#"
    assert main2(string) == Number(19)


# Valid complex equations
def test_complex_equation_1():
    string = "(3*(5-2)#)/((5!)/((-2^2)!)+1)"
    assert main2(string) == Number(1.5)


def test_complex_equation_2():
    string = "((1&2)^(2^3$-8)- 3!)*-(-2@6!#!)"
    assert main2(string) == Number(907195)


def test_complex_equation_3():
    string = "3!#^ 4 -(2^(-(2^2)@(3^3)))/100!"
    assert main2(string) == Number(1296)


def test_complex_equation_4():
    string = "((21/2)^2)#! - ~- ---120#!"
    assert main2(string) == Number(362874)


def test_complex_equation_5():
    string = "(10*(5@15))@((15%4)^(2^2))*((5%3)--(2 $3)&(2^ 3))"
    assert main2(string) == Number(452.5)


def test_complex_equation_6():
    string = "(((7!/6!)^2+1)- (40@((4*5)$60)))/((5%3)--(2 $3)&(2^ 3))"
    assert main2(string) == Number(0.0)


def test_complex_equation_7():
    string = "(19%(4!/4)+2)^(~---2! + 2^3 - (4^2)/2)*(7!/6!)^2+1)"
    assert main2(string) == Number(442)


def test_complex_equation_8():
    string = "((7 *(2^2))/2)@(5*(((3^2)*2)/6))"
    assert main2(string) == Number(14.5)


def test_complex_equation_9():
    string = "((7*3+2)#^-(-2&5)*2)*(5*2-4!#)*2&12"
    assert main2(string) == Number(400.0)


def test_complex_equation_10():
    string = "((2*2*2)*3!)-(((20^2)/2)/20)*6-((2^2*2^2)/110+~---4)"
    assert main2(string) == Number(-16.145454545454545)


def test_complex_equation_11():
    string = "(4!/2^3)^2+2^((20+6@(2^3))/3^2)"
    assert main2(string) == Number(17)


def test_complex_equation_12():
    string = "(6*3+1@(6^2/(2^2*3)))/(6!#-(8*5+1)#)&(2^24)"
    assert main2(string) == Number(5)


def test_complex_equation_13():
    string = "((102#!@-~     (3^2))*2)#!"
    assert main2(string) == Number(720)


def test_complex_equation_14():
    string = "(190915# * 5 / 5 ^ 2 @ 2 ^ 1) / 5 @ ~-2!! !!"
    assert main2(string) == Number(1.4285714285714286)


def test_complex_equation_15():
    string = "-(2^5)*(4!#+3)+((4^2*2^2)/110+~---4)"
    assert main2(string) == Number(-283.41818181818184)


def test_complex_equation_16():
    string = "3!#&89^5@(10--~2^3)!/(13%5$9)"
    assert main2(string) == Number(132.2724461102916)


def test_complex_equation_17():
    string = "(23$14)*120##+2^(2&10)-(0.5+1/(18%((5!+1)/13)))"
    assert main2(string) == Number(72.38495575221239)


def test_complex_equation_19():
    string = "3!#!#*(~-7!+5^5)@(-7^8$3!)"
    assert main2(string) == Number(25978347.0)


def test_complex_equation_20():
    string = "(~-3! + 2) @ -2  - (75.435 % 5)#"
    assert main2(string) == Number(-14)


# Run the test using the pytest command
pytest.main()
