from src.search.exceptions import NotFound


def fibonacci_search(array: list[int], value: int) -> int:
    fib_num_1 = 0
    fib_num_2 = 1
    fib_num_3 = fib_num_2 + fib_num_1
    while fib_num_3 < len(array):
        fib_num_1 = fib_num_2
        fib_num_2 = fib_num_3
        fib_num_3 = fib_num_2 + fib_num_1
    index = -1
    while fib_num_3 > 1:
        _index = min(index + fib_num_1, (len(array) - 1))
        if array[_index] < value:
            fib_num_3 = fib_num_2
            fib_num_2 = fib_num_1
            fib_num_1 = fib_num_3 - fib_num_2
            index = _index
        elif array[_index] > value:
            fib_num_3 = fib_num_1
            fib_num_2 = fib_num_2 - fib_num_1
            fib_num_1 = fib_num_3 - fib_num_2
        else:
            return _index
    if fib_num_2 and index < (len(array) - 1) and array[index + 1] == value:
        return index + 1
    raise NotFound
