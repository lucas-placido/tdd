import pytest


# Altere o scopo para entender
@pytest.fixture(scope="function")
def test_fixture_function():
    return [1]


def test_one_plus_one(test_fixture_function):
    test_fixture_function.append(1)
    assert sum(test_fixture_function) == 2


def test_one_plus_two(test_fixture_function):
    test_fixture_function.append(2)
    assert sum(test_fixture_function) == 3
