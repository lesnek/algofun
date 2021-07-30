from .binary import binary_search


def galloping_search(array: list[int], value: int) -> int:
    if array[0] == value:
        return 0
    index = 1
    while index < len(array) and array[index] <= value:
        index *= 2
    return binary_search(array[: min(index, len(array))], value)
