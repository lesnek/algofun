import math

from src.search.exceptions import NotFound


def jump_search(array: list[int], value: int) -> int:
    array_len = len(array)
    step = math.sqrt(array_len)
    previous = 0

    while array[int(min(step, array_len) - 1)] < value:
        previous = step
        step += math.sqrt(array_len)
        if previous >= array_len:
            raise NotFound

    while array[int(previous)] < value:
        previous += 1
        if previous == min(step, array_len):
            raise NotFound

    if array[int(previous)] == value:
        return int(previous)

    raise NotFound
