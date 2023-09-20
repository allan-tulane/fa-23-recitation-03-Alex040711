from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(5)) == 3*5
    assert quadratic_multiply(BinaryNumber(7), BinaryNumber(11)) == 7*11