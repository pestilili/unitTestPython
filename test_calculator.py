import pytest
from calculator import sum, substract, multiply, divide

#AAA //Arrange (bemenő adatok), act (függvény), assert 
def test_sum_AAA():
    num1 = 2
    num2 = 3 

    result = sum(num1, num2)  

    assert result  == 5

def test_sum():
    assert sum(2,3) == 5
    assert sum(2, -3) == -1
    assert sum(-2, -3) == -5
    assert sum(0, -3) == -3
    assert sum (0, 3) ==3

def test_subtract():
    assert substract(3,2) == 1
    assert substract(2,2) == 0
    assert substract(2, -3) == 5
    assert substract(-2,-3) == 1
    assert substract(0, -3) == 3

def test_multiply():
    assert multiply(3,2)==6
    assert multiply(3,-2)==-6
    assert multiply(-3,-2)==6
    assert multiply(3,0)==0

def test_divide():
    assert divide(10,5)==2
    assert divide(4,5)==0.8
    assert divide(10,-5)==-2
    assert divide(-10,-5)==2