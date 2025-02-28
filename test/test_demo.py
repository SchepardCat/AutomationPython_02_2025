import pytest

@pytest.fixture()
def before_after():
    #Предусловия
    print("Before test")
    yield
    #Постусловия
    print("\nAfter test")

def test_demo1():
    assert 1 == 1

def test_demo2(before_after):
    assert 2 == 2