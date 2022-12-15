# Import the pytest module
import pytest
from main import main2
from values import Number


# Write a test function to test the add function
def test_main2():
    # Test that the add function returns the expected result
    assert main2("-~(-3)*( 3!)") == Number(-18.0)
    assert main2("(5%3)--(2 $3)&(2^ 3)") == Number(5)


# Run the test using the pytest command
pytest.main()
