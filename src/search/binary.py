from src.search.exceptions import NotFound


def binary_search(array: list[int], value: int) -> int:
    first = 0
    last = len(array) - 1
    index = -1
    while first <= last and index == -1:
        mid = (first + last) // 2
        if array[mid] == value:
            index = mid
        elif value < array[mid]:
            last = mid - 1
        else:
            first = mid + 1

    if index != -1:
        return index
    else:
        raise NotFound

