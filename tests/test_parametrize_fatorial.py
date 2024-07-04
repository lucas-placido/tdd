import pytest
from tdd.parametrize import fatorial


@pytest.mark.parametrize(
    ("numero,result"),
    [(0, 1), (1, 1), (2, 2), (3, 6)],
)
def test_fatorial(numero: int, result: int):
    assert fatorial(numero) == result


@pytest.mark.parametrize("entrada_negativa", [-1, -2, -10])
def test_fatorial_negativo(entrada_negativa: int):
    with pytest.raises(RecursionError):
        fatorial(entrada_negativa)
