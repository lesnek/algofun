import pytest
from tests.unit.search import data
from src.search.linear import linear_search


@pytest.mark.parametrize(
    "array, value, result",
    [(data.SORTED_1, 2, 1), (data.SORTED_2, 81, 5), (data.SORTED_3, 167, 35)],
)
def test_binary_search(array, value, result):
    assert linear_search(array, value) == result
