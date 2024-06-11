# tests/test_module1.py
from my_package.module1 import func1

def test_func1():
    assert func1() == "Hello from module1!"
