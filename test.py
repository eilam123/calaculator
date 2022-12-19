# Import the pytest module
import pytest
from main import main2
from values import Number


# Write a test function to test the add function
def test_main2():
    # Test that the add function returns the expected result
    assert main2("-~(-3)*( 3!)") == Number(-18.0)
    assert main2("(5%3)--(2 $3)&(2^ 3)") == Number(5)
    assert main2("102#!@-~     (3^2)") == Number(7.5)
    # give me complex test cases with at least 20 characters


def test_addition_operator():
    string = "3+2\0"
    assert main2(string) == Number(5)


def test_subtraction_operator():
    string = "100-54\0"
    assert main2(string) == Number(46)


def test_multiplication_operator():
    string = "3*21\0"
    assert main2(string) == Number(63)


def test_division_operator():
    string = "15/2\0"
    assert main2(string) == 7.5


def test_power_operator():
    string = "-2^3\0"
    assert main2(string) == -8


def test_mod_operator():
    string = "19%7\0"
    assert main2(string) == 5


def test_max_operator():
    string = "4$10\0"
    assert main2(string) == 10


def test_min_operator():
    string = "3&2\0"
    assert main2(string) == 2


def test_avg_operator():
    string = "12@20\0"
    assert main2(string) == 16


def test_tilda_operator():
    string = "~--2\0"
    assert main2(string) == Number(-2)


def test_factorial_operator():
    string = "5!\0"
    assert main2(string) == 120


def test_sum_digits_operator():
    string = "15364#\0"
    assert main2(string) == 19


# Valid complex equations
def test_complex_equation_1():
    string = "(3*(5-2)!)/((5!)/((-2^2)!)+1)\0"
    assert main2(string) == Number(3.0)


def test_complex_equation_2():
    string = "((5&2)^(2^2$-4)- 3!)*-(-2@5!#!)\0"
    assert main2(string) == Number(-20.0)


def test_complex_equation_3():
    string = "4!#^ 2 -(2^(-(2^2)@(2^3)))!\0"
    assert main2(string) == Number(12.0)


def test_complex_equation_4():
    string = "((22/2)^2)#! - ~---120#!\0"
    assert main2(string) == Number(18.0)


def test_complex_equation_5():
    string = "(10*(5@15))@((15%4)^(2^2))\0"
    assert main2(string) == Number(90.5)


def test_complex_equation_6():
    string = "((7!/6!)^2+1)- (40@((4*5)$60))\0"
    assert main2(string) == Number(0.0)


def test_complex_equation_7():
    string = "(19%(4!/4)+2)^(~---2! + 2^3 - (4^2)/2)\0"
    assert main2(string) == Number(9)


def test_complex_equation_8():
    string = "((7 *(2^2))/2)@(5*(((3^2)*2)/6))\0"
    assert main2(string) == Number(14.5)


def test_complex_equation_9():
    string = "((7*3+2)#^-(-2&5)*2)*(5*2-4!#)\0"
    assert main2(string) == Number(200.0)


def test_complex_equation_10():
    string = "((2*2*2)*3!)-(((20^2)/2)/20)*6\0"
    assert main2(string) == Number(-12.0)


def test_complex_equation_11():
    string = "(4!/2^3)^2+2^((20+6@(2^3))/3^2)\0"
    assert main2(string) == Number(17)


def test_complex_equation_12():
    string = "(6*3+1@(6^2/(2^2*3)))/(6!#-(8*5+1)#)\0"
    assert main2(string) == Number(5)


def test_complex_equation_13():
    string = "(11^2)%((10+1!#)*((5*2^1)&(5*2^2)))\0"
    assert main2(string) == Number(11)


def test_complex_equation_14():
    string = "42%(6!#-(2^2*2^3+10)%(2^3+5&12))\0"
    assert main2(string) == Number(0)


def test_complex_equation_15():
    string = "-(2^3)*(5!#+3)+((5^2*2^2)/10+~---4)\0"
    assert main2(string) == Number(-34.0)


def test_complex_equation_16():
    string = "-((5+5+150%(40*3))*2@3)-(7*2^(11%(2^1*2^2)))\0"
    assert main2(string) == Number(-156)


def test_complex_equation_17():
    string = "-((10$4*3)*2^2+(25%(3*5)))+(20-(2^2)@(2*3))\0"
    assert main2(string) == Number(-115)


def test_complex_equation_18():
    string = "(30$14)*120#+2^(2&10)-(0.5+1/(16%((5!+1)/11)))\0"
    assert main2(string) == Number(93.3)


def test_complex_equation_19():
    string = "50*(0.04*10^2)+3-2^(~--5@(10+(10*10)#))\0"
    assert main2(string) == Number(195.0)


def test_complex_equation_20():
    string = "((10+10+10+3^2)/5!#)^2-(0.5*(2^-(-2&2)))\0"
    assert main2(string) == Number(167)


def test_complex_equation_21():
    string = "(~-3! + 2) @ -2  - (75.435 % 5)#\0"
    assert main2(string) == Number(-14)


# Run the test using the pytest command
pytest.main()
