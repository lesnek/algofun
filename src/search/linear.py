from src.search.exceptions import NotFound


def linear_search(array: list[int], value: int) -> int:
    for index in range(len(array)):
        if array[index] == value:
            return index
    raise NotFound
