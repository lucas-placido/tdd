from tdd.fixture import soma_dobro
import pytest


@pytest.fixture(scope="function")
def soma_dobro_fixture():
    return [1, 2, 3, 4, 5]


def test_soma_dobro(soma_dobro_fixture: list[int]):
    assert soma_dobro(soma_dobro_fixture) == 30
