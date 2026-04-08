import pytest
from app import divide_numbers, increment_counter

def test_divide_numbers():
    assert divide_numbers(10, 2) == 5
    assert divide_numbers(10, 0) == 0  # This will fail

def test_increment_counter():
    assert increment_counter() == 1
    assert increment_counter() == 2

def test_missing_test():
    # No assertion - bad test
    pass
