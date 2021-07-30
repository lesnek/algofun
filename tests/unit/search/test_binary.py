import pytest
from tests.unit.search import data
from src.search.binary import binary_search


@pytest.mark.parametrize(
    "array, value, result",
    [(data.SORTED_1, 2, 1), (data.SORTED_2, 81, 5), (data.SORTED_3, 167, 35)],
)
def test_binary_search(array, value, result):
    assert binary_search(array, value) == result
