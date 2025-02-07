import os
import sys
import pytest  

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fizzbuzz import fizzbuzz


def test_standard_cases():
    """Testes des cas de base"""
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"

def test_contains_3():
    """Testes si le nombre contient un 3"""
    assert fizzbuzz(12) == "Fizz"

def test_contains_5():
    """Testes si le nombre contient un 5"""
    assert fizzbuzz(59) == "59"
    assert fizzbuzz(60) == "FizzBuzz"

def test_contains_3_and_5():
    """Testes si le nombre contient à la fois un 3 et un 5"""
    assert fizzbuzz(45) == "FizzBuzz"