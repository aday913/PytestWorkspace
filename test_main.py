import pytest
import main

@pytest.fixture
def example():
    return main.testfunc1(1, 1)

def test_first_func(example):
    ans = example
    assert (ans == 2)

@pytest.fixture
def test2():
    return main.testfunc2(2,2)

def test_second_function(test2):
    multiple = test2
    assert multiple == 5

def test_random():
    assert True